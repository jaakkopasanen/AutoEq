# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.0; 41 -2.2; 45 -3.4; 49 -4.4; 54 -5.6; 60 -6.9; 66 -7.8; 72 -8.6; 79 -9.4; 87 -9.8; 96 -10.1; 106 -10.7; 116 -11.0; 128 -11.1; 141 -11.2; 155 -11.2; 170 -11.2; 187 -11.1; 206 -10.9; 227 -10.6; 249 -10.2; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.5; 535 -7.2; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.0; 1387 -7.6; 1526 -8.6; 1678 -9.3; 1846 -10.0; 2031 -10.6; 2234 -10.7; 2457 -9.9; 2703 -8.1; 2973 -5.7; 3270 -4.7; 3597 -5.6; 3957 -1.7; 4353 -1.9; 4788 -12.7; 5267 -7.5; 5793 -4.9; 6373 -4.3; 7010 -5.7; 7711 -6.2; 8482 -7.5; 9330 -11.3; 10263 -12.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.77 | 7.6 dB  |
| Peaking | 127 Hz  | 0.53 | -5.6 dB |
| Peaking | 2066 Hz | 2.69 | -4.7 dB |
| Peaking | 4108 Hz | 9.61 | 7.0 dB  |
| Peaking | 9907 Hz | 5.62 | -6.9 dB |
| Peaking | 775 Hz  | 2.15 | 0.9 dB  |
| Peaking | 2535 Hz | 4.41 | -1.6 dB |
| Peaking | 3149 Hz | 4    | 2.4 dB  |
| Peaking | 4890 Hz | 9.1  | -9.8 dB |
| Peaking | 5755 Hz | 2.3  | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)