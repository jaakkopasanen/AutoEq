# Creative Sound Blaster EVO ZxR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.2; 25 -5.1; 28 -6.2; 31 -7.2; 34 -8.0; 37 -8.8; 41 -9.6; 45 -10.4; 49 -11.0; 54 -11.7; 60 -12.4; 66 -13.0; 72 -13.5; 79 -13.9; 87 -14.5; 96 -14.9; 106 -15.4; 116 -15.9; 128 -16.3; 141 -16.6; 155 -17.0; 170 -17.2; 187 -17.3; 206 -17.3; 227 -17.2; 249 -17.1; 274 -16.9; 302 -17.1; 332 -16.9; 365 -16.1; 402 -15.2; 442 -14.2; 486 -13.0; 535 -11.5; 588 -10.0; 647 -8.2; 712 -6.4; 783 -5.2; 861 -5.8; 947 -6.1; 1042 -6.4; 1146 -5.8; 1261 -5.2; 1387 -3.9; 1526 -2.7; 1678 -1.7; 1846 -0.9; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.2; 2973 -4.0; 3270 -5.6; 3597 -4.8; 3957 -6.5; 4353 -8.4; 4788 -5.0; 5267 -6.3; 5793 -6.6; 6373 -7.6; 7010 -8.3; 7711 -11.6; 8482 -13.9; 9330 -12.6; 10263 -10.1; 11289 -9.1; 12418 -8.4; 13660 -7.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound Blaster EVO ZxR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound Blaster EVO ZxR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.03 | 4.4 dB  |
| Peaking | 135 Hz  | 0.48 | -9.5 dB |
| Peaking | 331 Hz  | 1.28 | -6.0 dB |
| Peaking | 2026 Hz | 1.23 | 6.7 dB  |
| Peaking | 8755 Hz | 2.26 | -7.7 dB |
| Peaking | 488 Hz  | 3.95 | -1.2 dB |
| Peaking | 760 Hz  | 4.69 | 2.9 dB  |
| Peaking | 2592 Hz | 9.34 | 1.5 dB  |
| Peaking | 4355 Hz | 5.2  | -4.4 dB |
| Peaking | 4746 Hz | 5.08 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -7.5 dB  |
| Peaking | 250 Hz   | 1.41 | -10.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20Blaster%20EVO%20ZxR/Creative%20Sound%20Blaster%20EVO%20ZxR.png)