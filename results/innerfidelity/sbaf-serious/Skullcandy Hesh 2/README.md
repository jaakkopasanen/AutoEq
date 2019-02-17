# Skullcandy Hesh 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.0; 25 -2.5; 28 -3.0; 31 -3.3; 34 -3.6; 37 -3.8; 41 -3.9; 45 -4.0; 49 -4.1; 54 -4.1; 60 -4.2; 66 -4.3; 72 -4.4; 79 -4.5; 87 -4.4; 96 -4.3; 106 -4.4; 116 -4.2; 128 -4.1; 141 -4.7; 155 -5.2; 170 -4.8; 187 -4.5; 206 -4.6; 227 -4.9; 249 -4.7; 274 -4.6; 302 -4.6; 332 -4.4; 365 -4.1; 402 -4.3; 442 -4.7; 486 -5.4; 535 -6.0; 588 -6.0; 647 -6.4; 712 -6.7; 783 -6.5; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -6.0; 1261 -5.6; 1387 -5.4; 1526 -5.4; 1678 -4.7; 1846 -3.9; 2031 -2.6; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.38 | 5.9 dB  |
| Peaking | 107 Hz  | 0.88 | 1.7 dB  |
| Peaking | 241 Hz  | 1.78 | 1.1 dB  |
| Peaking | 376 Hz  | 3.3  | 2.0 dB  |
| Peaking | 3693 Hz | 0.82 | 6.9 dB  |
| Peaking | 1031 Hz | 1.1  | -0.9 dB |
| Peaking | 2379 Hz | 3.81 | 2.0 dB  |
| Peaking | 3696 Hz | 2.77 | -1.1 dB |
| Peaking | 6246 Hz | 2.33 | 5.3 dB  |
| Peaking | 7417 Hz | 1.5  | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)