# Klipsch M40 Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.5; 31 -7.6; 34 -7.6; 37 -7.6; 41 -7.5; 45 -7.4; 49 -7.3; 54 -7.2; 60 -7.2; 66 -7.1; 72 -7.1; 79 -7.1; 87 -7.1; 96 -7.2; 106 -7.2; 116 -7.1; 128 -7.3; 141 -7.3; 155 -7.3; 170 -7.2; 187 -7.2; 206 -7.2; 227 -7.2; 249 -7.0; 274 -6.9; 302 -6.3; 332 -5.7; 365 -5.8; 402 -5.9; 442 -5.8; 486 -5.9; 535 -5.6; 588 -5.5; 647 -5.3; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.3; 1042 -6.8; 1146 -7.6; 1261 -8.6; 1387 -10.1; 1526 -11.8; 1678 -11.7; 1846 -9.3; 2031 -5.7; 2234 -3.1; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch M40 Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch M40 Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 1.03 | -1.0 dB  |
| Peaking | 203 Hz  | 0.67 | -1.5 dB  |
| Peaking | 425 Hz  | 0.55 | 1.4 dB   |
| Peaking | 1607 Hz | 2.04 | -10.1 dB |
| Peaking | 3130 Hz | 0.66 | 7.9 dB   |
| Peaking | 1929 Hz | 6.13 | -0.8 dB  |
| Peaking | 2439 Hz | 3.54 | 1.5 dB   |
| Peaking | 3322 Hz | 2.42 | -1.2 dB  |
| Peaking | 6307 Hz | 2.1  | 5.5 dB   |
| Peaking | 7339 Hz | 1.41 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20M40%20Mode/Klipsch%20M40%20Mode.png)