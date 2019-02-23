# Creative Sound Blaster EVO ZxR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.3; 28 -3.4; 31 -4.4; 34 -5.2; 37 -6.0; 41 -6.9; 45 -7.6; 49 -8.3; 54 -8.9; 60 -9.6; 66 -10.2; 72 -10.7; 79 -11.2; 87 -11.7; 96 -12.2; 106 -12.7; 116 -13.1; 128 -13.5; 141 -13.9; 155 -14.2; 170 -14.4; 187 -14.5; 206 -14.5; 227 -14.4; 249 -14.3; 274 -14.1; 302 -14.3; 332 -14.1; 365 -13.3; 402 -12.4; 442 -11.4; 486 -10.2; 535 -8.8; 588 -7.2; 647 -5.5; 712 -3.6; 783 -2.5; 861 -3.0; 947 -3.4; 1042 -3.6; 1146 -3.0; 1261 -2.5; 1387 -1.1; 1526 -0.8; 1678 -0.8; 1846 -0.8; 2031 -0.8; 2234 -0.8; 2457 -0.8; 2703 -0.8; 2973 -1.4; 3270 -2.9; 3597 -2.0; 3957 -3.7; 4353 -5.6; 4788 -2.2; 5267 -3.6; 5793 -3.8; 6373 -4.8; 7010 -5.5; 7711 -8.9; 8482 -11.1; 9330 -9.8; 10263 -7.3; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -6.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound Blaster EVO ZxR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound Blaster EVO ZxR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.91 | 7.5 dB  |
| Peaking | 289 Hz  | 0.26 | -9.0 dB |
| Peaking | 727 Hz  | 1.89 | 5.4 dB  |
| Peaking | 1684 Hz | 0.44 | 8.4 dB  |
| Peaking | 8546 Hz | 3.9  | -6.0 dB |
| Peaking | 511 Hz  | 5.48 | 0.4 dB  |
| Peaking | 1228 Hz | 2.81 | -0.7 dB |
| Peaking | 1417 Hz | 5.17 | 1.1 dB  |
| Peaking | 4307 Hz | 6.87 | -4.5 dB |
| Peaking | 4722 Hz | 3.09 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20Blaster%20EVO%20ZxR/Creative%20Sound%20Blaster%20EVO%20ZxR.png)