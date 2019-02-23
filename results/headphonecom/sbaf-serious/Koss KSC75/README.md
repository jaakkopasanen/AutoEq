# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.8; 49 -2.8; 54 -4.0; 60 -5.3; 66 -6.2; 72 -7.1; 79 -7.8; 87 -8.3; 96 -8.5; 106 -9.1; 116 -9.4; 128 -9.5; 141 -9.6; 155 -9.7; 170 -9.6; 187 -9.5; 206 -9.3; 227 -9.0; 249 -8.6; 274 -8.1; 302 -7.7; 332 -7.3; 365 -6.9; 402 -6.6; 442 -6.3; 486 -5.9; 535 -5.6; 588 -5.3; 647 -5.1; 712 -4.9; 783 -4.7; 861 -4.8; 947 -4.8; 1042 -5.0; 1146 -5.1; 1261 -5.4; 1387 -6.0; 1526 -7.0; 1678 -7.7; 1846 -8.4; 2031 -9.0; 2234 -9.1; 2457 -8.3; 2703 -6.5; 2973 -4.1; 3270 -3.1; 3597 -4.0; 3957 -0.9; 4353 -1.1; 4788 -11.1; 5267 -6.0; 5793 -3.3; 6373 -2.7; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -9.7; 10263 -10.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.75 | 7.0 dB  |
| Peaking | 125 Hz  |  0.8  | -4.1 dB |
| Peaking | 4018 Hz |  6.46 | 6.3 dB  |
| Peaking | 6329 Hz |  5.71 | 4.3 dB  |
| Peaking | 9852 Hz |  5.67 | -5.1 dB |
| Peaking | 240 Hz  |  1.98 | -1.0 dB |
| Peaking | 903 Hz  |  0.77 | 2.3 dB  |
| Peaking | 2308 Hz |  1.54 | -6.0 dB |
| Peaking | 2966 Hz |  1.77 | 5.1 dB  |
| Peaking | 4875 Hz | 12.73 | -7.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)