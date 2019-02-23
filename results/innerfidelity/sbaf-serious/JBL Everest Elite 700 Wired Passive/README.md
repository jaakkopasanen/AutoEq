# JBL Everest Elite 700 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.8; 25 -5.7; 28 -5.7; 31 -5.6; 34 -5.5; 37 -5.4; 41 -5.3; 45 -5.2; 49 -5.0; 54 -4.9; 60 -4.8; 66 -4.6; 72 -4.2; 79 -3.9; 87 -4.1; 96 -5.0; 106 -5.4; 116 -5.4; 128 -5.5; 141 -5.7; 155 -5.7; 170 -6.1; 187 -6.8; 206 -7.2; 227 -7.5; 249 -7.7; 274 -7.8; 302 -7.8; 332 -7.6; 365 -7.1; 402 -7.8; 442 -9.5; 486 -9.7; 535 -9.6; 588 -9.2; 647 -9.2; 712 -9.5; 783 -9.3; 861 -9.3; 947 -9.4; 1042 -9.6; 1146 -9.6; 1261 -10.2; 1387 -10.0; 1526 -10.1; 1678 -10.4; 1846 -10.7; 2031 -10.3; 2234 -9.8; 2457 -8.9; 2703 -7.6; 2973 -6.6; 3270 -4.8; 3597 -2.6; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -9.3; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 73 Hz   | 0.86 | 2.3 dB  |
| Peaking | 573 Hz  | 0.72 | -2.6 dB |
| Peaking | 1398 Hz | 1.23 | -2.1 dB |
| Peaking | 2122 Hz | 1.64 | -3.4 dB |
| Peaking | 4705 Hz | 1.54 | 7.5 dB  |
| Peaking | 238 Hz  | 4.85 | -0.6 dB |
| Peaking | 3816 Hz | 4.17 | 2.0 dB  |
| Peaking | 4604 Hz | 1.49 | -1.5 dB |
| Peaking | 6171 Hz | 4.66 | 3.2 dB  |
| Peaking | 9227 Hz | 3.88 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wired%20Passive/JBL%20Everest%20Elite%20700%20Wired%20Passive.png)