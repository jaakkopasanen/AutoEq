# Cougar Immersa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.9; 31 -2.7; 34 -3.5; 37 -4.1; 41 -4.9; 45 -5.6; 49 -6.2; 54 -6.9; 60 -7.7; 66 -8.5; 72 -9.4; 79 -10.4; 87 -11.4; 96 -12.2; 106 -12.8; 116 -13.2; 128 -13.5; 141 -13.7; 155 -13.6; 170 -13.4; 187 -13.0; 206 -12.6; 227 -12.2; 249 -11.7; 274 -11.2; 302 -11.0; 332 -10.5; 365 -9.7; 402 -8.6; 442 -7.6; 486 -6.9; 535 -6.1; 588 -5.3; 647 -4.6; 712 -4.1; 783 -4.0; 861 -3.6; 947 -3.2; 1042 -2.3; 1146 -0.9; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.6; 1846 -2.2; 2031 -4.1; 2234 -4.5; 2457 -3.6; 2703 -2.7; 2973 -2.3; 3270 -3.0; 3597 -5.2; 3957 -6.4; 4353 -6.4; 4788 -4.8; 5267 -4.8; 5793 -3.8; 6373 -3.6; 7010 -4.2; 7711 -6.5; 8482 -7.8; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.23 | 7.8 dB  |
| Peaking | 133 Hz  | 0.35 | -9.6 dB |
| Peaking | 911 Hz  | 0.41 | 4.3 dB  |
| Peaking | 1407 Hz | 2.12 | 3.5 dB  |
| Peaking | 2986 Hz | 5.19 | 2.7 dB  |
| Peaking | 624 Hz  | 4.9  | 0.5 dB  |
| Peaking | 4167 Hz | 4.59 | -2.1 dB |
| Peaking | 4842 Hz | 3.3  | 0.8 dB  |
| Peaking | 6493 Hz | 2.61 | 3.0 dB  |
| Peaking | 8255 Hz | 3.72 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cougar%20Immersa/Cougar%20Immersa.png)