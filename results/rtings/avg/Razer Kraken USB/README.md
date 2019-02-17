# Razer Kraken USB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.6; 31 -2.7; 34 -3.7; 37 -4.6; 41 -5.7; 45 -6.7; 49 -7.7; 54 -8.9; 60 -10.2; 66 -11.5; 72 -12.5; 79 -13.4; 87 -14.1; 96 -14.5; 106 -14.7; 116 -14.7; 128 -14.7; 141 -14.4; 155 -14.0; 170 -13.4; 187 -12.6; 206 -11.6; 227 -10.9; 249 -11.1; 274 -12.0; 302 -13.2; 332 -14.1; 365 -14.6; 402 -14.8; 442 -14.5; 486 -15.0; 535 -15.0; 588 -13.4; 647 -11.9; 712 -10.8; 783 -9.4; 861 -7.9; 947 -6.8; 1042 -6.3; 1146 -5.6; 1261 -4.8; 1387 -3.8; 1526 -2.7; 1678 -2.1; 1846 -2.2; 2031 -1.9; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.5; 6373 -9.0; 7010 -10.1; 7711 -10.4; 8482 -13.0; 9330 -13.3; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken USB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken USB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.86 | 7.0 dB   |
| Peaking | 102 Hz   | 0.72 | -8.6 dB  |
| Peaking | 478 Hz   | 1.02 | -8.8 dB  |
| Peaking | 4281 Hz  | 0.37 | 8.6 dB   |
| Peaking | 8242 Hz  | 1.39 | -12.9 dB |
| Peaking | 236 Hz   | 5.79 | 1.4 dB   |
| Peaking | 328 Hz   | 5.96 | -1.0 dB  |
| Peaking | 5499 Hz  | 5.84 | 3.1 dB   |
| Peaking | 6427 Hz  | 7.73 | -4.0 dB  |
| Peaking | 10862 Hz | 8.62 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -9.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)