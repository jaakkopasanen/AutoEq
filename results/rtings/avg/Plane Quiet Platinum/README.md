# Plane Quiet Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -7.5; 25 -8.8; 28 -9.8; 31 -9.9; 34 -9.6; 37 -9.2; 41 -8.6; 45 -8.1; 49 -7.7; 54 -7.4; 60 -7.4; 66 -7.3; 72 -7.2; 79 -7.2; 87 -7.2; 96 -7.3; 106 -7.5; 116 -7.7; 128 -7.8; 141 -7.8; 155 -7.7; 170 -7.6; 187 -7.2; 206 -7.0; 227 -7.0; 249 -6.8; 274 -6.1; 302 -5.8; 332 -5.4; 365 -5.0; 402 -4.7; 442 -4.5; 486 -4.3; 535 -4.1; 588 -4.2; 647 -4.4; 712 -4.9; 783 -4.9; 861 -4.6; 947 -5.5; 1042 -5.4; 1146 -5.6; 1261 -6.2; 1387 -5.8; 1526 -3.0; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plane Quiet Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plane Quiet Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.84 | -3.5 dB |
| Peaking | 138 Hz  | 1.18 | -1.3 dB |
| Peaking | 226 Hz  | 2.7  | -0.2 dB |
| Peaking | 474 Hz  | 1.52 | 2.2 dB  |
| Peaking | 3254 Hz | 0.65 | 6.9 dB  |
| Peaking | 1375 Hz | 2.98 | -4.6 dB |
| Peaking | 1642 Hz | 2.46 | 4.2 dB  |
| Peaking | 3220 Hz | 2.23 | -1.2 dB |
| Peaking | 6260 Hz | 2.06 | 5.7 dB  |
| Peaking | 7396 Hz | 1.43 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plane%20Quiet%20Platinum/Plane%20Quiet%20Platinum.png)