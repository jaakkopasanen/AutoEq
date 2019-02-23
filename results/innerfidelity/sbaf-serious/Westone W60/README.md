# Westone W60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.7; 28 -7.9; 31 -8.0; 34 -8.1; 37 -8.2; 41 -8.5; 45 -8.7; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.2; 87 -10.7; 96 -11.0; 106 -11.2; 116 -11.4; 128 -11.6; 141 -11.8; 155 -11.9; 170 -11.9; 187 -11.9; 206 -11.9; 227 -11.7; 249 -11.5; 274 -11.3; 302 -11.0; 332 -10.6; 365 -10.3; 402 -10.0; 442 -9.4; 486 -9.2; 535 -8.7; 588 -8.0; 647 -7.7; 712 -7.4; 783 -7.0; 861 -7.0; 947 -7.2; 1042 -7.6; 1146 -7.9; 1261 -8.4; 1387 -9.3; 1526 -9.9; 1678 -9.8; 1846 -8.7; 2031 -6.6; 2234 -4.2; 2457 -2.1; 2703 -1.5; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.0; 10263 -10.8; 11289 -7.6; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 75 Hz    | 0.15 | -0.8 dB |
| Peaking | 186 Hz   | 0.4  | -4.9 dB |
| Peaking | 1635 Hz  | 1.41 | -9.0 dB |
| Peaking | 3265 Hz  | 0.39 | 8.2 dB  |
| Peaking | 9846 Hz  | 1.98 | -6.8 dB |
| Peaking | 2515 Hz  | 7.53 | 1.0 dB  |
| Peaking | 4789 Hz  | 1.2  | -1.4 dB |
| Peaking | 6523 Hz  | 1.49 | 3.0 dB  |
| Peaking | 7458 Hz  | 4.58 | -3.8 dB |
| Peaking | 15179 Hz | 4.35 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W60/Westone%20W60.png)