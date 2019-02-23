# Aedle VK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.4; 49 -3.7; 54 -5.2; 60 -6.6; 66 -8.0; 72 -9.1; 79 -10.2; 87 -11.1; 96 -11.5; 106 -11.6; 116 -11.4; 128 -11.2; 141 -10.9; 155 -10.6; 170 -10.2; 187 -9.9; 206 -9.5; 227 -9.1; 249 -8.8; 274 -8.4; 302 -7.9; 332 -7.3; 365 -7.6; 402 -7.1; 442 -6.6; 486 -6.2; 535 -5.6; 588 -6.6; 647 -6.6; 712 -5.0; 783 -4.3; 861 -4.7; 947 -5.7; 1042 -6.9; 1146 -8.1; 1261 -9.5; 1387 -10.9; 1526 -12.0; 1678 -12.2; 1846 -10.6; 2031 -10.3; 2234 -9.2; 2457 -7.6; 2703 -5.9; 2973 -3.8; 3270 -2.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -2.2; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aedle VK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aedle VK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.55 | 9.5 dB  |
| Peaking | 89 Hz   | 0.6  | -8.8 dB |
| Peaking | 849 Hz  | 1.55 | 3.6 dB  |
| Peaking | 1644 Hz | 1.21 | -7.1 dB |
| Peaking | 4271 Hz | 1.19 | 7.6 dB  |
| Peaking | 502 Hz  | 6.29 | 0.8 dB  |
| Peaking | 3384 Hz | 2.53 | 1.9 dB  |
| Peaking | 4320 Hz | 1.18 | -2.2 dB |
| Peaking | 6035 Hz | 1.84 | 4.1 dB  |
| Peaking | 7670 Hz | 1.58 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aedle%20VK1/Aedle%20VK1.png)