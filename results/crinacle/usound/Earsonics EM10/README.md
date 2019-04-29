# Earsonics EM10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.9; 25 -9.9; 28 -9.9; 31 -9.8; 34 -9.8; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.0; 54 -10.1; 60 -10.3; 66 -10.4; 72 -10.5; 79 -10.7; 87 -10.9; 96 -11.2; 106 -11.2; 116 -11.2; 128 -11.2; 141 -11.1; 155 -10.8; 170 -10.5; 187 -10.0; 206 -9.4; 227 -8.8; 249 -8.2; 274 -7.6; 302 -7.1; 332 -6.9; 365 -6.7; 402 -6.7; 442 -6.9; 486 -7.1; 535 -7.3; 588 -7.6; 647 -7.8; 712 -8.0; 783 -8.1; 861 -8.4; 947 -8.9; 1042 -9.7; 1146 -10.9; 1261 -12.0; 1387 -12.3; 1526 -11.4; 1678 -9.5; 1846 -7.0; 2031 -4.4; 2234 -2.2; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -3.1; 3957 -3.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.0; 6373 -4.7; 7010 -9.0; 7711 -8.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -14.3; 18182 -17.3; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.4  | -4.7 dB  |
| Peaking | 1402 Hz  | 1.65 | -7.5 dB  |
| Peaking | 2607 Hz  | 1.48 | 7.6 dB   |
| Peaking | 4932 Hz  | 3.44 | 5.8 dB   |
| Peaking | 18343 Hz | 1.25 | -12.1 dB |
| Peaking | 23 Hz    | 2.43 | -1.6 dB  |
| Peaking | 159 Hz   | 2.36 | -1.1 dB  |
| Peaking | 333 Hz   | 2.1  | 1.3 dB   |
| Peaking | 7320 Hz  | 8.41 | -4.6 dB  |
| Peaking | 14045 Hz | 2.85 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20EM10/Earsonics%20EM10.png)