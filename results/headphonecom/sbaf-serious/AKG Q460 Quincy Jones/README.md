# AKG Q460 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.7; 25 -5.4; 28 -6.1; 31 -6.7; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.6; 49 -7.7; 54 -7.8; 60 -8.0; 66 -8.2; 72 -8.2; 79 -8.6; 87 -8.6; 96 -8.7; 106 -8.7; 116 -9.1; 128 -9.6; 141 -10.0; 155 -10.2; 170 -10.4; 187 -10.6; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -8.8; 365 -8.0; 402 -6.9; 442 -6.3; 486 -5.8; 535 -4.7; 588 -3.5; 647 -2.6; 712 -2.2; 783 -3.0; 861 -4.5; 947 -6.1; 1042 -6.3; 1146 -6.7; 1261 -6.7; 1387 -6.1; 1526 -5.2; 1678 -3.9; 1846 -2.4; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -2.8; 3597 -5.7; 3957 -6.2; 4353 -4.6; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.98 | 3.1 dB  |
| Peaking | 185 Hz  | 0.56 | -4.0 dB |
| Peaking | 654 Hz  | 2.27 | 5.2 dB  |
| Peaking | 2407 Hz | 2    | 6.7 dB  |
| Peaking | 5677 Hz | 3.04 | 6.5 dB  |
| Peaking | 1140 Hz | 0.96 | 1.4 dB  |
| Peaking | 1170 Hz | 1.94 | -2.9 dB |
| Peaking | 3802 Hz | 1.68 | 2.6 dB  |
| Peaking | 3876 Hz | 4.18 | -5.1 dB |
| Peaking | 8273 Hz | 3.43 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q460%20Quincy%20Jones/AKG%20Q460%20Quincy%20Jones.png)