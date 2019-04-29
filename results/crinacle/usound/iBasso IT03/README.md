# iBasso IT03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.6; 25 -12.5; 28 -12.2; 31 -11.9; 34 -11.6; 37 -11.3; 41 -11.0; 45 -10.6; 49 -10.3; 54 -10.0; 60 -9.7; 66 -9.5; 72 -9.4; 79 -9.3; 87 -9.2; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.1; 155 -9.2; 170 -9.1; 187 -9.0; 206 -8.9; 227 -8.8; 249 -8.7; 274 -8.5; 302 -8.3; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.7; 486 -7.4; 535 -7.3; 588 -7.0; 647 -6.7; 712 -6.4; 783 -6.1; 861 -5.8; 947 -5.8; 1042 -6.1; 1146 -6.8; 1261 -7.5; 1387 -7.9; 1526 -8.0; 1678 -7.5; 1846 -6.4; 2031 -4.7; 2234 -3.1; 2457 -2.0; 2703 -1.8; 2973 -2.4; 3270 -2.7; 3597 -0.7; 3957 -0.5; 4353 -1.1; 4788 -5.8; 5267 -7.7; 5793 -6.8; 6373 -5.0; 7010 -7.5; 7711 -11.6; 8482 -9.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -8.9; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.32 | -6.4 dB |
| Peaking | 183 Hz   | 0.7  | -2.2 dB |
| Peaking | 2545 Hz  | 2.45 | 6.3 dB  |
| Peaking | 3931 Hz  | 2.32 | 9.4 dB  |
| Peaking | 3995 Hz  | 0.54 | -3.9 dB |
| Peaking | 911 Hz   | 2.68 | 1.5 dB  |
| Peaking | 1473 Hz  | 3.41 | -1.5 dB |
| Peaking | 7796 Hz  | 1.78 | 4.1 dB  |
| Peaking | 7880 Hz  | 5.02 | -8.4 dB |
| Peaking | 18852 Hz | 2    | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT03/iBasso%20IT03.png)