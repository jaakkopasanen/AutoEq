# AKG Q350 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.9; 25 -9.3; 28 -9.8; 31 -10.1; 34 -10.4; 37 -10.6; 41 -10.9; 45 -11.1; 49 -11.4; 54 -11.6; 60 -11.9; 66 -12.1; 72 -12.2; 79 -12.4; 87 -12.5; 96 -12.6; 106 -12.5; 116 -12.4; 128 -12.4; 141 -12.2; 155 -12.0; 170 -11.7; 187 -11.3; 206 -10.8; 227 -10.3; 249 -9.8; 274 -9.2; 302 -8.5; 332 -7.8; 365 -7.0; 402 -6.3; 442 -5.5; 486 -4.8; 535 -4.1; 588 -3.3; 647 -2.6; 712 -2.0; 783 -1.5; 861 -1.3; 947 -1.0; 1042 -1.1; 1146 -1.1; 1261 -1.1; 1387 -1.4; 1526 -1.8; 1678 -1.8; 1846 -1.6; 2031 -1.2; 2234 -0.8; 2457 -0.6; 2703 -0.5; 2973 -0.9; 3270 -2.0; 3597 -4.1; 3957 -5.5; 4353 -6.8; 4788 -8.6; 5267 -11.0; 5793 -14.2; 6373 -9.5; 7010 -6.2; 7711 -5.9; 8482 -9.3; 9330 -11.1; 10263 -6.4; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q350 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q350 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.4  | -3.8 dB |
| Peaking | 163 Hz  | 0.47 | -4.6 dB |
| Peaking | 918 Hz  | 0.6  | 5.6 dB  |
| Peaking | 2691 Hz | 1.79 | 4.6 dB  |
| Peaking | 5645 Hz | 3.23 | -8.4 dB |
| Peaking | 7261 Hz | 5.14 | 2.7 dB  |
| Peaking | 9057 Hz | 5.64 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q350%20Quincy%20Jones/AKG%20Q350%20Quincy%20Jones.png)