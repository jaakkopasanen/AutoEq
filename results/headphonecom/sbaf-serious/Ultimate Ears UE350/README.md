# Ultimate Ears UE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.6; 23 -16.6; 25 -16.5; 28 -16.5; 31 -16.4; 34 -16.3; 37 -16.3; 41 -16.2; 45 -16.1; 49 -16.1; 54 -16.0; 60 -16.0; 66 -16.0; 72 -15.9; 79 -15.9; 87 -15.8; 96 -15.6; 106 -15.4; 116 -15.2; 128 -14.9; 141 -14.7; 155 -14.4; 170 -14.0; 187 -13.6; 206 -13.1; 227 -12.7; 249 -12.2; 274 -11.6; 302 -11.1; 332 -10.4; 365 -9.8; 402 -9.3; 442 -8.8; 486 -8.3; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.7; 783 -6.5; 861 -6.6; 947 -6.1; 1042 -6.8; 1146 -6.7; 1261 -6.6; 1387 -7.1; 1526 -7.8; 1678 -8.1; 1846 -8.0; 2031 -7.7; 2234 -7.1; 2457 -6.3; 2703 -5.0; 2973 -3.2; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.21 | -9.7 dB |
| Peaking | 162 Hz  | 0.57 | -4.7 dB |
| Peaking | 3629 Hz | 3.12 | 5.4 dB  |
| Peaking | 5780 Hz | 1.83 | 6.7 dB  |
| Peaking | 7916 Hz | 2.04 | -2.3 dB |
| Peaking | 841 Hz  | 1.45 | 1.0 dB  |
| Peaking | 1847 Hz | 1.75 | -2.1 dB |
| Peaking | 3085 Hz | 7    | 1.4 dB  |
| Peaking | 4305 Hz | 8.61 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE350/Ultimate%20Ears%20UE350.png)