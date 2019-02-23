# AKG Q460 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -7.2; 25 -7.9; 28 -8.6; 31 -9.1; 34 -9.5; 37 -9.7; 41 -9.9; 45 -10.1; 49 -10.2; 54 -10.3; 60 -10.5; 66 -10.7; 72 -10.7; 79 -11.1; 87 -11.1; 96 -11.2; 106 -11.2; 116 -11.6; 128 -12.1; 141 -12.5; 155 -12.7; 170 -12.9; 187 -13.1; 206 -12.9; 227 -12.6; 249 -12.5; 274 -12.2; 302 -11.8; 332 -11.3; 365 -10.5; 402 -9.4; 442 -8.8; 486 -8.3; 535 -7.2; 588 -6.0; 647 -5.1; 712 -4.7; 783 -5.5; 861 -7.0; 947 -8.6; 1042 -8.8; 1146 -9.2; 1261 -9.2; 1387 -8.6; 1526 -7.7; 1678 -6.4; 1846 -4.9; 2031 -3.3; 2234 -2.3; 2457 -1.4; 2703 -1.2; 2973 -2.7; 3270 -5.3; 3597 -8.2; 3957 -8.7; 4353 -7.1; 4788 -4.0; 5267 -0.5; 5793 -1.0; 6373 -1.2; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 0.45 | -4.0 dB |
| Peaking | 223 Hz  | 1.04 | -5.1 dB |
| Peaking | 1239 Hz | 3.26 | -3.3 dB |
| Peaking | 2453 Hz | 3.05 | 5.9 dB  |
| Peaking | 5769 Hz | 3.77 | 6.5 dB  |
| Peaking | 350 Hz  | 3.18 | -1.1 dB |
| Peaking | 696 Hz  | 2.95 | 3.1 dB  |
| Peaking | 969 Hz  | 4.97 | -1.9 dB |
| Peaking | 3837 Hz | 1.48 | 3.4 dB  |
| Peaking | 3864 Hz | 3.38 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q460%20Quincy%20Jones/AKG%20Q460%20Quincy%20Jones.png)