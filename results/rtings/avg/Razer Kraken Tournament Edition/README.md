# Razer Kraken Tournament Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.2; 41 -2.4; 45 -3.7; 49 -5.0; 54 -6.4; 60 -7.9; 66 -9.0; 72 -9.9; 79 -10.7; 87 -11.4; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.4; 141 -12.3; 155 -12.2; 170 -12.0; 187 -11.7; 206 -11.3; 227 -10.9; 249 -10.5; 274 -9.9; 302 -9.7; 332 -10.9; 365 -11.7; 402 -12.4; 442 -13.0; 486 -13.4; 535 -12.5; 588 -11.0; 647 -9.5; 712 -7.5; 783 -6.2; 861 -5.4; 947 -3.8; 1042 -2.4; 1146 -1.1; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.2; 4353 -1.2; 4788 -4.2; 5267 -5.3; 5793 -5.8; 6373 -3.4; 7010 -4.0; 7711 -8.2; 8482 -11.9; 9330 -10.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Tournament Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Tournament Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.63 | 8.8 dB  |
| Peaking | 99 Hz    | 0.51 | -7.8 dB |
| Peaking | 512 Hz   | 1.19 | -9.3 dB |
| Peaking | 1629 Hz  | 0.34 | 7.2 dB  |
| Peaking | 8707 Hz  | 4.25 | -7.5 dB |
| Peaking | 289 Hz   | 7.97 | 1.1 dB  |
| Peaking | 4285 Hz  | 2.68 | 3.3 dB  |
| Peaking | 5204 Hz  | 1.95 | -3.9 dB |
| Peaking | 6679 Hz  | 6.35 | 3.7 dB  |
| Peaking | 14576 Hz | 2.2  | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -7.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20Tournament%20Edition/Razer%20Kraken%20Tournament%20Edition.png)