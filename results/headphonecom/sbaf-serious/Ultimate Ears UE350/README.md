# Ultimate Ears UE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.8; 28 -15.7; 31 -15.6; 34 -15.6; 37 -15.5; 41 -15.4; 45 -15.4; 49 -15.3; 54 -15.3; 60 -15.2; 66 -15.2; 72 -15.2; 79 -15.1; 87 -15.0; 96 -14.9; 106 -14.6; 116 -14.4; 128 -14.1; 141 -14.0; 155 -13.6; 170 -13.3; 187 -12.9; 206 -12.4; 227 -11.9; 249 -11.4; 274 -10.8; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.5; 442 -8.0; 486 -7.6; 535 -7.1; 588 -6.6; 647 -6.1; 712 -5.9; 783 -5.8; 861 -5.8; 947 -5.3; 1042 -6.0; 1146 -5.9; 1261 -5.8; 1387 -6.4; 1526 -7.0; 1678 -7.3; 1846 -7.2; 2031 -6.9; 2234 -6.4; 2457 -5.5; 2703 -4.2; 2973 -2.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.44 | -7.2 dB |
| Peaking | 105 Hz  | 0.3  | -7.4 dB |
| Peaking | 711 Hz  | 0.55 | 2.2 dB  |
| Peaking | 1900 Hz | 1.56 | -3.0 dB |
| Peaking | 4223 Hz | 1.06 | 7.0 dB  |
| Peaking | 3274 Hz | 6.29 | 1.7 dB  |
| Peaking | 4329 Hz | 2.88 | -0.9 dB |
| Peaking | 6321 Hz | 2.37 | 4.5 dB  |
| Peaking | 7350 Hz | 0.74 | -1.4 dB |
| Peaking | 7523 Hz | 2.93 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE350/Ultimate%20Ears%20UE350.png)