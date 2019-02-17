# Klipsch Image S4i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.8; 25 -12.8; 28 -12.9; 31 -12.9; 34 -12.9; 37 -12.9; 41 -12.9; 45 -13.0; 49 -13.2; 54 -13.4; 60 -13.5; 66 -13.7; 72 -13.9; 79 -14.1; 87 -14.2; 96 -14.4; 106 -14.4; 116 -14.4; 128 -14.5; 141 -14.4; 155 -14.3; 170 -14.1; 187 -13.8; 206 -13.4; 227 -13.0; 249 -12.5; 274 -12.0; 302 -11.2; 332 -10.5; 365 -9.7; 402 -9.0; 442 -8.2; 486 -7.4; 535 -6.6; 588 -5.9; 647 -5.2; 712 -4.5; 783 -4.1; 861 -4.0; 947 -4.0; 1042 -4.3; 1146 -4.6; 1261 -5.0; 1387 -5.6; 1526 -6.2; 1678 -6.3; 1846 -5.9; 2031 -5.9; 2234 -5.7; 2457 -5.3; 2703 -5.0; 2973 -4.0; 3270 -2.1; 3597 -0.5; 3957 -0.9; 4353 -2.9; 4788 -4.5; 5267 -6.0; 5793 -8.6; 6373 -7.4; 7010 -4.0; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -5.6; 11289 -4.8; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.21 | -8.1 dB |
| Peaking | 134 Hz   | 0.62 | -6.1 dB |
| Peaking | 274 Hz   | 1.02 | -3.8 dB |
| Peaking | 3756 Hz  | 5.22 | 4.5 dB  |
| Peaking | 5894 Hz  | 5.18 | -5.2 dB |
| Peaking | 872 Hz   | 1.89 | 1.7 dB  |
| Peaking | 1803 Hz  | 1.18 | -2.1 dB |
| Peaking | 3326 Hz  | 6.88 | 1.5 dB  |
| Peaking | 7302 Hz  | 7.48 | 1.5 dB  |
| Peaking | 10602 Hz | 8.98 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4i/Klipsch%20Image%20S4i.png)