# Creative Sound Blaster EVO ZxR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.8; 28 -2.9; 31 -3.9; 34 -4.7; 37 -5.5; 41 -6.4; 45 -7.1; 49 -7.8; 54 -8.4; 60 -9.1; 66 -9.7; 72 -10.1; 79 -10.6; 87 -11.1; 96 -11.6; 106 -12.1; 116 -12.5; 128 -12.9; 141 -13.3; 155 -13.6; 170 -13.8; 187 -14.0; 206 -14.0; 227 -14.0; 249 -13.9; 274 -13.7; 302 -14.0; 332 -13.9; 365 -13.1; 402 -12.1; 442 -11.0; 486 -9.9; 535 -8.5; 588 -7.0; 647 -5.2; 712 -3.4; 783 -2.3; 861 -2.7; 947 -3.2; 1042 -3.4; 1146 -2.9; 1261 -2.3; 1387 -0.9; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.0; 3270 -2.2; 3597 -1.6; 3957 -3.2; 4353 -4.7; 4788 -2.5; 5267 -3.6; 5793 -3.5; 6373 -3.4; 7010 -5.3; 7711 -9.4; 8482 -10.5; 9330 -7.8; 10263 -6.5; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound Blaster EVO ZxR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound Blaster EVO ZxR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.97 | 6.5 dB  |
| Peaking | 280 Hz  | 0.27 | -8.5 dB |
| Peaking | 738 Hz  | 1.38 | 8.1 dB  |
| Peaking | 1576 Hz | 1.14 | 5.8 dB  |
| Peaking | 2957 Hz | 1    | 4.5 dB  |
| Peaking | 1402 Hz | 2.52 | 0.1 dB  |
| Peaking | 4232 Hz | 9.9  | -2.2 dB |
| Peaking | 6586 Hz | 1.72 | 3.5 dB  |
| Peaking | 8096 Hz | 3.26 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20Blaster%20EVO%20ZxR/Creative%20Sound%20Blaster%20EVO%20ZxR.png)