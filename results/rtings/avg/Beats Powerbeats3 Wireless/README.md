# Beats Powerbeats3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.2; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.7; 41 -5.8; 45 -5.8; 49 -5.7; 54 -5.7; 60 -5.8; 66 -5.9; 72 -5.9; 79 -5.9; 87 -5.9; 96 -6.0; 106 -6.0; 116 -6.0; 128 -6.0; 141 -5.9; 155 -5.8; 170 -5.6; 187 -5.3; 206 -4.9; 227 -4.6; 249 -4.1; 274 -3.7; 302 -3.3; 332 -3.0; 365 -2.7; 402 -2.3; 442 -1.8; 486 -1.6; 535 -1.8; 588 -2.0; 647 -2.3; 712 -2.8; 783 -3.0; 861 -3.3; 947 -4.0; 1042 -4.8; 1146 -5.5; 1261 -6.2; 1387 -6.6; 1526 -6.8; 1678 -6.8; 1846 -6.7; 2031 -6.6; 2234 -6.2; 2457 -5.0; 2703 -3.5; 2973 -2.0; 3270 -1.0; 3597 -0.9; 3957 -1.5; 4353 -2.8; 4788 -4.5; 5267 -5.2; 5793 -2.1; 6373 -0.5; 7010 -1.4; 7711 -3.6; 8482 -3.8; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 117 Hz   | 0.23 | -2.6 dB |
| Peaking | 543 Hz   | 0.63 | 4.8 dB  |
| Peaking | 2146 Hz  | 0.45 | -5.3 dB |
| Peaking | 3340 Hz  | 1.72 | 7.4 dB  |
| Peaking | 6488 Hz  | 4.36 | 4.9 dB  |
| Peaking | 284 Hz   | 5.13 | 0.2 dB  |
| Peaking | 4081 Hz  | 7.69 | 0.7 dB  |
| Peaking | 5102 Hz  | 8    | -1.9 dB |
| Peaking | 10188 Hz | 0.69 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats3%20Wireless/Beats%20Powerbeats3%20Wireless.png)