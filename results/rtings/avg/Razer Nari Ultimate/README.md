# Razer Nari Ultimate
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.7; 34 -5.8; 37 -6.0; 41 -6.4; 45 -7.0; 49 -7.5; 54 -8.0; 60 -8.5; 66 -8.9; 72 -9.5; 79 -10.2; 87 -10.9; 96 -11.4; 106 -11.7; 116 -11.9; 128 -12.0; 141 -12.1; 155 -12.0; 170 -11.9; 187 -11.6; 206 -11.1; 227 -10.5; 249 -9.7; 274 -9.4; 302 -9.0; 332 -8.5; 365 -7.8; 402 -6.8; 442 -6.2; 486 -6.0; 535 -5.7; 588 -4.6; 647 -3.8; 712 -4.0; 783 -4.1; 861 -3.9; 947 -3.1; 1042 -2.7; 1146 -2.4; 1261 -2.2; 1387 -2.2; 1526 -2.8; 1678 -3.9; 1846 -5.2; 2031 -6.2; 2234 -6.7; 2457 -6.0; 2703 -4.7; 2973 -3.9; 3270 -4.0; 3597 -5.8; 3957 -7.9; 4353 -5.1; 4788 -3.6; 5267 -2.9; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -7.0; 18182 -9.2; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Nari Ultimate GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Nari Ultimate ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 1.17 | -3.5 dB |
| Peaking | 181 Hz   | 0.84 | -4.9 dB |
| Peaking | 1104 Hz  | 0.91 | 4.2 dB  |
| Peaking | 6084 Hz  | 2.84 | 6.3 dB  |
| Peaking | 16402 Hz | 0.03 | -0.8 dB |
| Peaking | 22 Hz    | 1.54 | 1.3 dB  |
| Peaking | 2265 Hz  | 2.62 | -4.3 dB |
| Peaking | 2743 Hz  | 1.27 | 3.4 dB  |
| Peaking | 3905 Hz  | 7.13 | -4.0 dB |
| Peaking | 17798 Hz | 3.71 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Nari%20Ultimate/Razer%20Nari%20Ultimate.png)