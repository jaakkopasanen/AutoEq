# Sony MDR-7509HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -2.5; 79 -3.7; 87 -4.9; 96 -5.5; 106 -5.4; 116 -5.7; 128 -6.4; 141 -7.5; 155 -8.4; 170 -7.5; 187 -8.2; 206 -7.8; 227 -7.7; 249 -7.3; 274 -6.7; 302 -6.2; 332 -6.4; 365 -7.6; 402 -8.8; 442 -9.5; 486 -9.7; 535 -9.2; 588 -7.7; 647 -6.0; 712 -7.4; 783 -6.5; 861 -6.2; 947 -6.0; 1042 -6.0; 1146 -6.4; 1261 -7.0; 1387 -8.3; 1526 -10.4; 1678 -11.9; 1846 -12.2; 2031 -13.3; 2234 -12.7; 2457 -10.4; 2703 -7.4; 2973 -5.5; 3270 -3.9; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -10.3; 9330 -11.0; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7509HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.83 | 7.2 dB  |
| Peaking | 2055 Hz | 1.9  | -8.4 dB |
| Peaking | 4149 Hz | 1.43 | 7.2 dB  |
| Peaking | 6417 Hz | 5.56 | 4.1 dB  |
| Peaking | 8983 Hz | 4.17 | -6.2 dB |
| Peaking | 37 Hz   | 3.67 | -1.4 dB |
| Peaking | 61 Hz   | 3.35 | 2.4 dB  |
| Peaking | 167 Hz  | 1.86 | -2.2 dB |
| Peaking | 473 Hz  | 3.42 | -3.6 dB |
| Peaking | 1015 Hz | 2.75 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)