# Turtle Beach Recon 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.6; 25 -9.7; 28 -9.8; 31 -9.7; 34 -9.4; 37 -9.0; 41 -8.5; 45 -8.1; 49 -7.7; 54 -7.4; 60 -7.5; 66 -8.2; 72 -9.1; 79 -10.2; 87 -11.5; 96 -12.4; 106 -13.0; 116 -13.1; 128 -12.8; 141 -12.3; 155 -11.6; 170 -10.7; 187 -9.7; 206 -8.5; 227 -7.1; 249 -5.9; 274 -4.6; 302 -3.3; 332 -2.1; 365 -1.7; 402 -1.8; 442 -2.5; 486 -2.6; 535 -2.5; 588 -2.4; 647 -2.2; 712 -2.2; 783 -2.0; 861 -1.8; 947 -0.8; 1042 -1.5; 1146 -1.7; 1261 -0.5; 1387 -2.6; 1526 -2.8; 1678 -3.0; 1846 -3.5; 2031 -3.8; 2234 -3.6; 2457 -3.7; 2703 -4.1; 2973 -4.9; 3270 -6.2; 3597 -6.6; 3957 -6.8; 4353 -6.4; 4788 -2.0; 5267 -3.1; 5793 -5.6; 6373 -8.1; 7010 -8.2; 7711 -6.5; 8482 -7.0; 9330 -7.9; 10263 -7.3; 11289 -7.0; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -2.1; 18182 -0.5; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.75 | -8.5 dB  |
| Peaking | 122 Hz   | 0.81 | -12.3 dB |
| Peaking | 3144 Hz  | 0.94 | -4.1 dB  |
| Peaking | 9082 Hz  | 0.84 | -6.6 dB  |
| Peaking | 14501 Hz | 2.1  | -4.2 dB  |
| Peaking | 197 Hz   | 3.73 | -1.1 dB  |
| Peaking | 345 Hz   | 4.75 | 1.9 dB   |
| Peaking | 4278 Hz  | 4.03 | -4.4 dB  |
| Peaking | 4789 Hz  | 3.44 | 5.4 dB   |
| Peaking | 6395 Hz  | 5.65 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -12.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Recon%20200/Turtle%20Beach%20Recon%20200.png)