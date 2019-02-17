# Ultrasone HFI-580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.7; 28 -3.0; 31 -4.1; 34 -5.2; 37 -6.0; 41 -6.9; 45 -7.5; 49 -7.9; 54 -8.3; 60 -8.3; 66 -8.3; 72 -7.5; 79 -5.7; 87 -6.2; 96 -6.6; 106 -6.8; 116 -6.6; 128 -6.0; 141 -5.4; 155 -4.8; 170 -2.9; 187 -2.3; 206 -5.8; 227 -6.1; 249 -6.7; 274 -7.6; 302 -8.1; 332 -8.0; 365 -7.5; 402 -7.1; 442 -6.8; 486 -6.7; 535 -6.7; 588 -6.5; 647 -6.3; 712 -6.1; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.3; 1146 -5.2; 1261 -6.2; 1387 -6.9; 1526 -7.7; 1678 -8.9; 1846 -10.2; 2031 -10.7; 2234 -10.5; 2457 -10.2; 2703 -10.7; 2973 -12.0; 3270 -13.7; 3597 -12.8; 3957 -11.4; 4353 -9.4; 4788 -6.8; 5267 -3.5; 5793 -0.8; 6373 -0.9; 7010 -3.8; 7711 -8.4; 8482 -11.6; 9330 -13.3; 10263 -11.9; 11289 -6.9; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.84 | 6.2 dB  |
| Peaking | 1986 Hz  | 3.38 | -3.2 dB |
| Peaking | 3460 Hz  | 1.76 | -7.7 dB |
| Peaking | 6061 Hz  | 2.48 | 8.7 dB  |
| Peaking | 9140 Hz  | 2.66 | -8.4 dB |
| Peaking | 57 Hz    | 2.64 | -2.5 dB |
| Peaking | 178 Hz   | 4.7  | 4.5 dB  |
| Peaking | 310 Hz   | 2.55 | -2.0 dB |
| Peaking | 1164 Hz  | 5.7  | 1.6 dB  |
| Peaking | 11864 Hz | 6.07 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)