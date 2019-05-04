# Beats Powerbeats3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.0; 25 -11.1; 28 -11.2; 31 -11.4; 34 -11.5; 37 -11.5; 41 -11.5; 45 -11.5; 49 -11.4; 54 -11.2; 60 -10.9; 66 -10.7; 72 -10.5; 79 -10.3; 87 -10.1; 96 -9.8; 106 -9.5; 116 -9.1; 128 -8.7; 141 -8.3; 155 -7.7; 170 -7.2; 187 -6.6; 206 -6.1; 227 -5.5; 249 -5.0; 274 -4.6; 302 -4.3; 332 -3.9; 365 -3.5; 402 -3.2; 442 -2.7; 486 -2.6; 535 -2.8; 588 -3.0; 647 -3.4; 712 -3.8; 783 -4.1; 861 -4.4; 947 -5.0; 1042 -5.9; 1146 -6.7; 1261 -7.4; 1387 -7.8; 1526 -8.0; 1678 -8.0; 1846 -7.9; 2031 -8.0; 2234 -8.0; 2457 -6.8; 2703 -5.1; 2973 -3.0; 3270 -1.7; 3597 -1.6; 3957 -2.1; 4353 -3.4; 4788 -5.9; 5267 -6.6; 5793 -3.2; 6373 -0.5; 7010 -2.5; 7711 -4.8; 8482 -5.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.24 | -6.4 dB |
| Peaking | 571 Hz  | 0.51 | 4.6 dB  |
| Peaking | 2033 Hz | 0.43 | -5.8 dB |
| Peaking | 3401 Hz | 1.92 | 8.1 dB  |
| Peaking | 6461 Hz | 5.05 | 6.2 dB  |
| Peaking | 4215 Hz | 7.84 | 1.1 dB  |
| Peaking | 5093 Hz | 7.54 | -2.3 dB |
| Peaking | 9890 Hz | 0.77 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats3%20Wireless/Beats%20Powerbeats3%20Wireless.png)