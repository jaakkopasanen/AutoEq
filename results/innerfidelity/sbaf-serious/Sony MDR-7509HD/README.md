# Sony MDR-7509HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.7; 72 -2.9; 79 -4.2; 87 -5.4; 96 -5.9; 106 -5.8; 116 -6.1; 128 -6.8; 141 -7.9; 155 -8.8; 170 -8.0; 187 -8.7; 206 -8.2; 227 -8.1; 249 -7.7; 274 -7.1; 302 -6.7; 332 -6.9; 365 -8.0; 402 -9.2; 442 -9.9; 486 -10.1; 535 -9.6; 588 -8.1; 647 -6.4; 712 -7.8; 783 -7.0; 861 -6.6; 947 -6.4; 1042 -6.5; 1146 -6.9; 1261 -7.4; 1387 -8.7; 1526 -10.8; 1678 -12.3; 1846 -12.6; 2031 -13.7; 2234 -13.1; 2457 -10.8; 2703 -7.8; 2973 -6.0; 3270 -4.4; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.3; 5793 -2.4; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -10.8; 9330 -11.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7509HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.92 | 7.2 dB  |
| Peaking | 2048 Hz | 1.71 | -8.6 dB |
| Peaking | 4152 Hz | 1.5  | 7.4 dB  |
| Peaking | 6396 Hz | 5.58 | 4.3 dB  |
| Peaking | 8927 Hz | 4.12 | -6.7 dB |
| Peaking | 37 Hz   | 3.52 | -1.4 dB |
| Peaking | 60 Hz   | 3.15 | 2.6 dB  |
| Peaking | 172 Hz  | 1.61 | -2.5 dB |
| Peaking | 473 Hz  | 3.07 | -3.8 dB |
| Peaking | 1051 Hz | 2.84 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)