# Audio-Technica ATH-ANC27x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -21.5; 23 -21.6; 25 -21.5; 28 -21.1; 31 -20.3; 34 -19.4; 37 -18.6; 41 -17.9; 45 -17.6; 49 -17.3; 54 -16.6; 60 -15.9; 66 -15.4; 72 -15.0; 79 -14.6; 87 -14.2; 96 -14.0; 106 -13.9; 116 -13.9; 128 -13.7; 141 -13.5; 155 -13.2; 170 -12.9; 187 -12.5; 206 -12.1; 227 -11.8; 249 -11.5; 274 -11.2; 302 -10.8; 332 -10.4; 365 -9.9; 402 -9.4; 442 -8.9; 486 -8.6; 535 -8.2; 588 -7.7; 647 -6.8; 712 -5.7; 783 -5.2; 861 -5.5; 947 -5.8; 1042 -6.6; 1146 -6.6; 1261 -6.2; 1387 -4.6; 1526 -2.0; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.8; 2973 -3.2; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -2.8; 5793 -7.0; 6373 -12.2; 7010 -11.8; 7711 -11.8; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.7; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.36 | -15.0 dB |
| Peaking | 183 Hz   | 0.56 | -4.4 dB  |
| Peaking | 1930 Hz  | 1.79 | 5.6 dB   |
| Peaking | 4725 Hz  | 1.09 | 8.7 dB   |
| Peaking | 6677 Hz  | 2.08 | -11.5 dB |
| Peaking | 792 Hz   | 3.52 | 2.1 dB   |
| Peaking | 1259 Hz  | 1.85 | -1.9 dB  |
| Peaking | 1573 Hz  | 5.73 | 2.3 dB   |
| Peaking | 9160 Hz  | 7.84 | 1.5 dB   |
| Peaking | 12366 Hz | 8.29 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)