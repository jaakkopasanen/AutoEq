# iBasso IT03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.8; 25 -13.6; 28 -13.3; 31 -13.0; 34 -12.7; 37 -12.4; 41 -12.1; 45 -11.8; 49 -11.5; 54 -11.1; 60 -10.9; 66 -10.7; 72 -10.5; 79 -10.4; 87 -10.4; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.2; 187 -10.2; 206 -10.0; 227 -9.9; 249 -9.8; 274 -9.7; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.7; 442 -8.5; 486 -8.2; 535 -8.0; 588 -7.7; 647 -7.4; 712 -7.1; 783 -6.7; 861 -6.5; 947 -6.6; 1042 -6.9; 1146 -7.5; 1261 -8.0; 1387 -8.1; 1526 -7.9; 1678 -7.4; 1846 -6.2; 2031 -4.2; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -4.9; 5267 -6.8; 5793 -5.7; 6373 -3.5; 7010 -5.2; 7711 -8.6; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -17.4; 16529 -24.6; 18182 -25.4; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.35 | -7.3 dB  |
| Peaking | 188 Hz   | 0.53 | -3.1 dB  |
| Peaking | 3308 Hz  | 1.02 | 10.2 dB  |
| Peaking | 12943 Hz | 0.41 | 26.8 dB  |
| Peaking | 16672 Hz | 0.26 | -37.2 dB |
| Peaking | 1626 Hz  | 1.55 | -5.2 dB  |
| Peaking | 3201 Hz  | 2.52 | -5.9 dB  |
| Peaking | 3265 Hz  | 0.57 | 7.4 dB   |
| Peaking | 5845 Hz  | 1.3  | -8.3 dB  |
| Peaking | 6434 Hz  | 4.43 | 7.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -18.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT03/iBasso%20IT03.png)