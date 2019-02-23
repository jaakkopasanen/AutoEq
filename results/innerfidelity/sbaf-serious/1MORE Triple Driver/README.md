# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.1; 25 -6.5; 28 -7.0; 31 -7.5; 34 -7.8; 37 -8.1; 41 -8.5; 45 -8.8; 49 -9.1; 54 -9.3; 60 -9.6; 66 -10.0; 72 -10.2; 79 -10.5; 87 -10.9; 96 -11.1; 106 -11.2; 116 -11.2; 128 -11.3; 141 -11.3; 155 -11.2; 170 -11.0; 187 -10.7; 206 -10.4; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.1; 442 -6.3; 486 -6.0; 535 -5.4; 588 -4.7; 647 -4.3; 712 -4.1; 783 -3.8; 861 -3.9; 947 -4.2; 1042 -4.5; 1146 -4.6; 1261 -5.0; 1387 -5.8; 1526 -6.7; 1678 -7.5; 1846 -8.0; 2031 -8.4; 2234 -9.0; 2457 -9.0; 2703 -8.6; 2973 -6.9; 3270 -5.2; 3597 -5.1; 3957 -7.4; 4353 -9.8; 4788 -7.2; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.7; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.7; 16529 -9.2; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 75 Hz    | 0.76 | -2.3 dB |
| Peaking | 164 Hz   | 0.64 | -3.9 dB |
| Peaking | 823 Hz   | 0.86 | 4.8 dB  |
| Peaking | 3013 Hz  | 0.21 | -2.5 dB |
| Peaking | 5953 Hz  | 2.81 | 9.0 dB  |
| Peaking | 18 Hz    | 2.4  | 1.4 dB  |
| Peaking | 2578 Hz  | 1.91 | -3.9 dB |
| Peaking | 3444 Hz  | 1.46 | 5.5 dB  |
| Peaking | 4338 Hz  | 4.88 | -6.6 dB |
| Peaking | 16367 Hz | 3.64 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)