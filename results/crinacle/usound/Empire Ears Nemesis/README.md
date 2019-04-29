# Empire Ears Nemesis
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.2; 25 -14.1; 28 -13.9; 31 -13.7; 34 -13.5; 37 -13.3; 41 -13.1; 45 -12.9; 49 -12.7; 54 -12.4; 60 -12.1; 66 -12.0; 72 -11.9; 79 -11.7; 87 -11.6; 96 -11.5; 106 -11.3; 116 -11.1; 128 -10.9; 141 -10.6; 155 -10.4; 170 -10.0; 187 -9.6; 206 -9.2; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.3; 332 -6.8; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.1; 535 -4.7; 588 -4.2; 647 -3.9; 712 -3.3; 783 -3.0; 861 -2.9; 947 -3.3; 1042 -4.1; 1146 -5.2; 1261 -6.3; 1387 -7.1; 1526 -7.4; 1678 -7.3; 1846 -7.1; 2031 -6.7; 2234 -6.2; 2457 -5.6; 2703 -4.9; 2973 -4.0; 3270 -2.8; 3597 -1.1; 3957 -0.5; 4353 -1.5; 4788 -1.8; 5267 -0.5; 5793 -6.5; 6373 -10.4; 7010 -12.5; 7711 -15.2; 8482 -13.2; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -9.9; 16529 -13.0; 18182 -16.2; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Nemesis GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Nemesis ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.36 | -7.5 dB  |
| Peaking | 130 Hz   |  1.23 | -2.8 dB  |
| Peaking | 4484 Hz  |  1.36 | 7.1 dB   |
| Peaking | 7478 Hz  |  2.79 | -10.7 dB |
| Peaking | 18585 Hz |  1.01 | -10.9 dB |
| Peaking | 837 Hz   |  1.18 | 4.4 dB   |
| Peaking | 1529 Hz  |  1.35 | -2.7 dB  |
| Peaking | 5326 Hz  | 16.09 | 3.0 dB   |
| Peaking | 8403 Hz  |  7.27 | -2.6 dB  |
| Peaking | 10798 Hz |  2.04 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Nemesis/Empire%20Ears%20Nemesis.png)