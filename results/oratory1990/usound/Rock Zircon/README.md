# Rock Zircon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.0; 25 -3.2; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.2; 60 -5.6; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.6; 106 -7.9; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.0; 170 -6.8; 187 -8.2; 206 -8.2; 227 -7.6; 249 -6.8; 274 -6.0; 302 -5.2; 332 -4.4; 365 -3.7; 402 -3.0; 442 -2.4; 486 -1.8; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.7; 947 -1.1; 1042 -1.8; 1146 -2.6; 1261 -3.5; 1387 -4.4; 1526 -5.1; 1678 -5.5; 1846 -5.5; 2031 -5.4; 2234 -5.4; 2457 -6.3; 2703 -6.9; 2973 -7.9; 3270 -7.5; 3597 -6.6; 3957 -5.9; 4353 -6.0; 4788 -7.6; 5267 -11.3; 5793 -15.2; 6373 -12.9; 7010 -12.3; 7711 -13.5; 8482 -10.2; 9330 -4.0; 10263 -1.4; 11289 -1.4; 12418 -4.6; 13660 -10.9; 15026 -13.2; 16529 -13.0; 18182 -11.8; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 0.64 | -6.2 dB  |
| Peaking | 219 Hz   | 1.82 | -3.8 dB  |
| Peaking | 2539 Hz  | 1.11 | -4.6 dB  |
| Peaking | 6294 Hz  | 1.9  | -12.2 dB |
| Peaking | 17099 Hz | 0.86 | -12.9 dB |
| Peaking | 761 Hz   | 1.64 | 2.0 dB   |
| Peaking | 1488 Hz  | 3.19 | -1.9 dB  |
| Peaking | 8088 Hz  | 4.45 | -7.3 dB  |
| Peaking | 10899 Hz | 1.32 | 6.6 dB   |
| Peaking | 14006 Hz | 2.45 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.1 dB  |
| Peaking | 16000 Hz | 1.41 | -13.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Rock%20Zircon/Rock%20Zircon.png)