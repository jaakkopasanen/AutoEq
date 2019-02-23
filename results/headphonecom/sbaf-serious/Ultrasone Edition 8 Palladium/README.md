# Ultrasone Edition 8 Palladium
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.0; 49 -1.9; 54 -3.3; 60 -4.4; 66 -3.9; 72 -4.6; 79 -5.8; 87 -6.7; 96 -7.6; 106 -8.3; 116 -9.0; 128 -9.4; 141 -9.8; 155 -9.0; 170 -9.5; 187 -9.3; 206 -9.3; 227 -8.6; 249 -9.6; 274 -8.4; 302 -7.9; 332 -7.3; 365 -6.3; 402 -5.7; 442 -5.4; 486 -4.9; 535 -4.5; 588 -4.5; 647 -5.8; 712 -5.5; 783 -5.3; 861 -5.6; 947 -5.6; 1042 -5.7; 1146 -5.9; 1261 -6.0; 1387 -6.1; 1526 -6.1; 1678 -5.7; 1846 -5.3; 2031 -1.9; 2234 -0.5; 2457 -2.6; 2703 -6.8; 2973 -5.4; 3270 -4.4; 3597 -6.4; 3957 -10.8; 4353 -8.1; 4788 -6.4; 5267 -2.6; 5793 -3.3; 6373 -9.9; 7010 -9.8; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 8 Palladium GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 Palladium ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.59 | 6.6 dB  |
| Peaking | 141 Hz  | 1.02 | -4.3 dB |
| Peaking | 2214 Hz | 4.39 | 6.7 dB  |
| Peaking | 5516 Hz | 6.09 | 13.0 dB |
| Peaking | 5876 Hz | 2.08 | -7.0 dB |
| Peaking | 262 Hz  | 3.01 | -1.8 dB |
| Peaking | 526 Hz  | 1.31 | 2.1 dB  |
| Peaking | 3338 Hz | 8.04 | 2.6 dB  |
| Peaking | 3974 Hz | 9.27 | -4.2 dB |
| Peaking | 8552 Hz | 4.43 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20Edition%208%20Palladium/Ultrasone%20Edition%208%20Palladium.png)