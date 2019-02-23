# Klipsch Image S4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -12.0; 28 -12.0; 31 -12.0; 34 -12.1; 37 -12.2; 41 -12.3; 45 -12.4; 49 -12.5; 54 -12.8; 60 -13.0; 66 -13.2; 72 -13.4; 79 -13.5; 87 -13.8; 96 -13.9; 106 -13.9; 116 -13.9; 128 -13.9; 141 -13.8; 155 -13.7; 170 -13.5; 187 -13.3; 206 -12.9; 227 -12.4; 249 -11.9; 274 -11.4; 302 -10.7; 332 -10.0; 365 -9.2; 402 -8.5; 442 -7.9; 486 -7.3; 535 -6.6; 588 -5.9; 647 -5.1; 712 -4.4; 783 -3.9; 861 -3.6; 947 -3.7; 1042 -3.8; 1146 -4.0; 1261 -4.3; 1387 -4.8; 1526 -5.5; 1678 -5.9; 1846 -6.0; 2031 -6.2; 2234 -6.3; 2457 -5.9; 2703 -5.2; 2973 -3.8; 3270 -1.6; 3597 -0.5; 3957 -0.6; 4353 -2.6; 4788 -4.2; 5267 -5.4; 5793 -7.1; 6373 -4.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -10.2; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.96 | -5.0 dB |
| Peaking | 50 Hz    | 0.38 | -4.4 dB |
| Peaking | 169 Hz   | 0.53 | -5.4 dB |
| Peaking | 845 Hz   | 1.16 | 3.8 dB  |
| Peaking | 3725 Hz  | 2.81 | 6.5 dB  |
| Peaking | 1252 Hz  | 5.69 | 0.7 dB  |
| Peaking | 2157 Hz  | 3.37 | -0.9 dB |
| Peaking | 5852 Hz  | 7.96 | -2.0 dB |
| Peaking | 6736 Hz  | 7.72 | 3.3 dB  |
| Peaking | 14660 Hz | 3.91 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4/Klipsch%20Image%20S4.png)