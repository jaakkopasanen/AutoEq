# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.7; 25 -4.6; 28 -4.6; 31 -4.7; 34 -4.7; 37 -4.5; 41 -4.5; 45 -4.9; 49 -5.1; 54 -5.2; 60 -5.5; 66 -6.0; 72 -6.4; 79 -6.6; 87 -6.7; 96 -7.2; 106 -7.5; 116 -7.6; 128 -7.8; 141 -7.7; 155 -7.7; 170 -7.5; 187 -7.2; 206 -6.4; 227 -6.5; 249 -6.9; 274 -7.1; 302 -7.0; 332 -6.8; 365 -6.7; 402 -6.7; 442 -6.9; 486 -7.0; 535 -6.8; 588 -6.7; 647 -6.5; 712 -6.4; 783 -6.4; 861 -6.5; 947 -6.8; 1042 -7.0; 1146 -7.3; 1261 -7.5; 1387 -7.6; 1526 -7.2; 1678 -7.0; 1846 -7.3; 2031 -7.5; 2234 -7.1; 2457 -6.0; 2703 -6.2; 2973 -6.4; 3270 -6.6; 3597 -6.7; 3957 -5.2; 4353 -2.9; 4788 -1.9; 5267 -2.0; 5793 -1.2; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.9; 10263 -10.0; 11289 -11.5; 12418 -12.4; 13660 -17.4; 15026 -23.9; 16529 -29.0; 18182 -29.7; 20000 -24.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.48 | 3.2 dB   |
| Peaking | 96 Hz    | 0.52 | -3.7 dB  |
| Peaking | 2820 Hz  | 0.4  | -9.2 dB  |
| Peaking | 6270 Hz  | 0.36 | 19.6 dB  |
| Peaking | 17343 Hz | 0.31 | -29.8 dB |
| Peaking | 3625 Hz  | 3.42 | -3.2 dB  |
| Peaking | 3983 Hz  | 0.97 | 1.8 dB   |
| Peaking | 7599 Hz  | 7    | -2.5 dB  |
| Peaking | 12488 Hz | 6.19 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -32.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)