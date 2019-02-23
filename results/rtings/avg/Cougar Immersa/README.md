# Cougar Immersa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.2; 28 -2.1; 31 -3.0; 34 -3.7; 37 -4.3; 41 -5.1; 45 -5.8; 49 -6.4; 54 -7.0; 60 -7.8; 66 -8.7; 72 -9.6; 79 -10.6; 87 -11.6; 96 -12.4; 106 -13.0; 116 -13.5; 128 -13.8; 141 -13.9; 155 -13.8; 170 -13.6; 187 -13.2; 206 -12.7; 227 -12.2; 249 -11.7; 274 -11.3; 302 -11.1; 332 -10.5; 365 -9.7; 402 -8.7; 442 -7.6; 486 -6.8; 535 -6.0; 588 -5.2; 647 -4.4; 712 -4.0; 783 -3.9; 861 -3.5; 947 -3.1; 1042 -2.2; 1146 -0.8; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.9; 2031 -3.7; 2234 -3.6; 2457 -2.7; 2703 -2.1; 2973 -2.3; 3270 -3.3; 3597 -5.3; 3957 -6.6; 4353 -6.9; 4788 -4.4; 5267 -4.5; 5793 -3.6; 6373 -4.7; 7010 -4.3; 7711 -6.2; 8482 -8.1; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -7.0; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.2  | 7.8 dB   |
| Peaking | 129 Hz  | 0.36 | -10.0 dB |
| Peaking | 950 Hz  | 0.44 | 4.3 dB   |
| Peaking | 1421 Hz | 1.94 | 3.2 dB   |
| Peaking | 2874 Hz | 4.71 | 2.8 dB   |
| Peaking | 626 Hz  | 5.38 | 0.5 dB   |
| Peaking | 4302 Hz | 3.98 | -3.9 dB  |
| Peaking | 4827 Hz | 2.19 | 2.8 dB   |
| Peaking | 6820 Hz | 3.3  | 1.5 dB   |
| Peaking | 8779 Hz | 4.51 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cougar%20Immersa/Cougar%20Immersa.png)