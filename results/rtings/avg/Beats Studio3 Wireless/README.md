# Beats Studio3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.3; 25 -3.8; 28 -4.5; 31 -5.1; 34 -5.7; 37 -6.1; 41 -6.7; 45 -7.2; 49 -7.7; 54 -8.3; 60 -9.1; 66 -9.6; 72 -9.9; 79 -9.8; 87 -9.7; 96 -9.3; 106 -8.9; 116 -8.5; 128 -8.3; 141 -8.4; 155 -8.7; 170 -9.0; 187 -9.4; 206 -9.7; 227 -10.1; 249 -10.5; 274 -10.9; 302 -11.1; 332 -11.5; 365 -11.6; 402 -10.8; 442 -9.5; 486 -7.9; 535 -6.3; 588 -5.1; 647 -4.7; 712 -5.3; 783 -5.6; 861 -6.0; 947 -6.4; 1042 -6.0; 1146 -5.5; 1261 -5.6; 1387 -5.3; 1526 -5.1; 1678 -4.9; 1846 -4.9; 2031 -4.8; 2234 -4.3; 2457 -3.6; 2703 -4.0; 2973 -6.6; 3270 -8.1; 3597 -7.8; 3957 -5.2; 4353 -2.3; 4788 -0.5; 5267 -1.4; 5793 -2.0; 6373 -2.8; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.9; 11289 -11.9; 12418 -11.1; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.36 | 4.9 dB  |
| Peaking | 68 Hz    | 0.63 | -4.2 dB |
| Peaking | 312 Hz   | 1.83 | -5.1 dB |
| Peaking | 5196 Hz  | 2.22 | 6.0 dB  |
| Peaking | 11718 Hz | 3.62 | -6.5 dB |
| Peaking | 412 Hz   | 4.26 | -1.9 dB |
| Peaking | 620 Hz   | 3.09 | 2.5 dB  |
| Peaking | 2370 Hz  | 0.75 | 1.9 dB  |
| Peaking | 2576 Hz  | 5.05 | 1.8 dB  |
| Peaking | 3365 Hz  | 3.47 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)