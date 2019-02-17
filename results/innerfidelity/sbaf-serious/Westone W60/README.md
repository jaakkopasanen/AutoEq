# Westone W60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.7; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.3; 41 -7.5; 45 -7.7; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.7; 96 -10.1; 106 -10.3; 116 -10.5; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.0; 187 -11.0; 206 -10.9; 227 -10.7; 249 -10.6; 274 -10.3; 302 -10.0; 332 -9.7; 365 -9.4; 402 -9.0; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.1; 647 -6.7; 712 -6.5; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -8.9; 1678 -8.8; 1846 -7.7; 2031 -5.7; 2234 -3.3; 2457 -1.2; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.1; 10263 -9.9; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 113 Hz  | 0.64 | -2.1 dB |
| Peaking | 246 Hz  | 0.52 | -3.4 dB |
| Peaking | 1615 Hz | 1.51 | -8.4 dB |
| Peaking | 3245 Hz | 0.36 | 8.1 dB  |
| Peaking | 9669 Hz | 1.6  | -6.0 dB |
| Peaking | 1974 Hz | 5.75 | -0.8 dB |
| Peaking | 2496 Hz | 3.32 | 1.4 dB  |
| Peaking | 4049 Hz | 1.22 | -1.1 dB |
| Peaking | 6672 Hz | 1.82 | 2.5 dB  |
| Peaking | 7379 Hz | 5.02 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W60/Westone%20W60.png)