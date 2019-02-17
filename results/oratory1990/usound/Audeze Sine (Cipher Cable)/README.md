# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -2.7; 25 -2.6; 28 -2.6; 31 -2.7; 34 -2.7; 37 -2.5; 41 -2.5; 45 -2.9; 49 -3.2; 54 -3.3; 60 -3.5; 66 -4.0; 72 -4.4; 79 -4.6; 87 -4.7; 96 -5.3; 106 -5.5; 116 -5.6; 128 -5.8; 141 -5.7; 155 -5.7; 170 -5.5; 187 -5.2; 206 -4.4; 227 -4.5; 249 -4.9; 274 -5.1; 302 -5.0; 332 -5.0; 365 -5.0; 402 -5.0; 442 -5.2; 486 -5.4; 535 -5.3; 588 -5.2; 647 -5.0; 712 -4.9; 783 -4.9; 861 -4.9; 947 -5.1; 1042 -5.3; 1146 -5.7; 1261 -6.2; 1387 -6.6; 1526 -6.4; 1678 -6.3; 1846 -6.7; 2031 -7.2; 2234 -7.4; 2457 -6.9; 2703 -7.5; 2973 -7.8; 3270 -8.0; 3597 -7.9; 3957 -5.9; 4353 -3.3; 4788 -1.9; 5267 -2.1; 5793 -1.5; 6373 -0.5; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -6.8; 11289 -9.2; 12418 -9.1; 13660 -7.6; 15026 -6.7; 16529 -9.2; 18182 -12.3; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.88 | 3.0 dB  |
| Peaking | 3333 Hz  | 1.48 | -3.7 dB |
| Peaking | 5527 Hz  | 1.13 | 8.0 dB  |
| Peaking | 17751 Hz | 0.06 | -3.2 dB |
| Peaking | 19062 Hz | 1.28 | -4.9 dB |
| Peaking | 135 Hz   | 1.95 | -0.9 dB |
| Peaking | 216 Hz   | 3.83 | 1.0 dB  |
| Peaking | 783 Hz   | 2.81 | 0.7 dB  |
| Peaking | 11724 Hz | 4.83 | -2.3 dB |
| Peaking | 14929 Hz | 3.51 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -5.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)