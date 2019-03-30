# Philips O Neill SHO 9560
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.6; 66 -1.9; 72 -1.9; 79 -1.9; 87 -2.1; 96 -2.4; 106 -2.6; 116 -2.5; 128 -2.6; 141 -2.8; 155 -2.5; 170 -1.9; 187 -1.3; 206 -1.1; 227 -1.6; 249 -3.1; 274 -5.5; 302 -8.3; 332 -10.9; 365 -13.5; 402 -15.2; 442 -16.1; 486 -16.2; 535 -16.0; 588 -15.4; 647 -14.7; 712 -13.9; 783 -12.9; 861 -11.3; 947 -9.4; 1042 -7.4; 1146 -5.5; 1261 -4.0; 1387 -2.7; 1526 -1.9; 1678 -1.6; 1846 -1.4; 2031 -1.4; 2234 -1.6; 2457 -1.6; 2703 -2.2; 2973 -3.5; 3270 -4.4; 3597 -3.9; 3957 -4.3; 4353 -6.2; 4788 -5.7; 5267 -2.1; 5793 -1.3; 6373 -5.8; 7010 -9.1; 7711 -10.5; 8482 -10.7; 9330 -11.1; 10263 -11.5; 11289 -10.8; 12418 -9.9; 13660 -9.6; 15026 -9.3; 16529 -7.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips O Neill SHO 9560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips O Neill SHO 9560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 58 Hz    | 0.23 | 8.2 dB   |
| Peaking | 224 Hz   | 1    | 13.3 dB  |
| Peaking | 487 Hz   | 0.32 | -21.4 dB |
| Peaking | 1547 Hz  | 0.47 | 15.2 dB  |
| Peaking | 10208 Hz | 1.06 | -6.1 dB  |
| Peaking | 566 Hz   | 6.08 | 0.7 dB   |
| Peaking | 4655 Hz  | 2.98 | -3.2 dB  |
| Peaking | 5573 Hz  | 4.03 | 7.1 dB   |
| Peaking | 7220 Hz  | 3.82 | -2.7 dB  |
| Peaking | 20421 Hz | 2.07 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 3.4 dB   |
| Peaking | 125 Hz   | 1.41 | 3.4 dB   |
| Peaking | 250 Hz   | 1.41 | 5.1 dB   |
| Peaking | 500 Hz   | 1.41 | -13.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20O%20Neill%20SHO%209560/Philips%20O%20Neill%20SHO%209560.png)