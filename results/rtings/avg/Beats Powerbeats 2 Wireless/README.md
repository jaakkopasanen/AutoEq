# Beats Powerbeats 2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.9; 28 -6.4; 31 -6.8; 34 -7.2; 37 -7.5; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.8; 60 -9.5; 66 -10.3; 72 -10.9; 79 -11.5; 87 -12.2; 96 -12.9; 106 -13.6; 116 -14.2; 128 -14.9; 141 -15.6; 155 -16.1; 170 -16.5; 187 -16.7; 206 -16.8; 227 -16.7; 249 -16.4; 274 -16.0; 302 -15.4; 332 -14.8; 365 -14.0; 402 -12.9; 442 -11.7; 486 -10.1; 535 -8.0; 588 -6.1; 647 -4.2; 712 -2.3; 783 -1.0; 861 -0.5; 947 -1.0; 1042 -1.6; 1146 -1.9; 1261 -2.1; 1387 -2.1; 1526 -2.3; 1678 -3.0; 1846 -4.8; 2031 -6.5; 2234 -6.7; 2457 -6.0; 2703 -4.2; 2973 -2.2; 3270 -1.5; 3597 -1.3; 3957 -1.7; 4353 -2.8; 4788 -5.0; 5267 -7.0; 5793 -6.9; 6373 -7.7; 7010 -8.8; 7711 -9.3; 8482 -6.6; 9330 -2.0; 10263 -1.3; 11289 -1.3; 12418 -1.3; 13660 -1.3; 15026 -1.3; 16529 -1.3; 18182 -1.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.39 | -8.2 dB |
| Peaking | 201 Hz   | 0.95 | -9.9 dB |
| Peaking | 369 Hz   | 1.77 | -7.0 dB |
| Peaking | 2187 Hz  | 3.73 | -5.7 dB |
| Peaking | 6905 Hz  | 1.95 | -8.2 dB |
| Peaking | 509 Hz   | 4    | -1.9 dB |
| Peaking | 827 Hz   | 2.29 | 3.1 dB  |
| Peaking | 3677 Hz  | 2.31 | 4.7 dB  |
| Peaking | 4002 Hz  | 1.14 | -3.2 dB |
| Peaking | 10173 Hz | 3.57 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.5 dB  |
| Peaking | 125 Hz   | 1.41 | -10.5 dB |
| Peaking | 250 Hz   | 1.41 | -14.2 dB |
| Peaking | 500 Hz   | 1.41 | -5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 16000 Hz | 1.41 | 1.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)