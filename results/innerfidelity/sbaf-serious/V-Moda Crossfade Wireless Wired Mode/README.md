# V-Moda Crossfade Wireless Wired Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.8; 25 -5.4; 28 -6.3; 31 -7.1; 34 -7.7; 37 -8.2; 41 -8.8; 45 -9.3; 49 -9.6; 54 -9.9; 60 -10.1; 66 -10.0; 72 -9.6; 79 -10.6; 87 -11.9; 96 -11.7; 106 -11.5; 116 -12.4; 128 -12.9; 141 -13.0; 155 -12.8; 170 -12.1; 187 -12.0; 206 -11.3; 227 -10.0; 249 -8.5; 274 -6.8; 302 -5.1; 332 -3.3; 365 -1.2; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -1.3; 712 -2.6; 783 -3.6; 861 -4.9; 947 -6.0; 1042 -6.9; 1146 -7.5; 1261 -8.1; 1387 -8.7; 1526 -9.2; 1678 -9.4; 1846 -9.0; 2031 -8.5; 2234 -8.7; 2457 -8.6; 2703 -7.6; 2973 -8.5; 3270 -9.8; 3597 -10.7; 3957 -7.7; 4353 -5.0; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -10.9; 10263 -9.6; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Wired Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Wired Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 178 Hz  | 0.51 | -10.2 dB |
| Peaking | 445 Hz  | 0.66 | 13.1 dB  |
| Peaking | 1952 Hz | 0.32 | -4.9 dB  |
| Peaking | 5573 Hz | 1.9  | 9.9 dB   |
| Peaking | 9331 Hz | 3.88 | -5.1 dB  |
| Peaking | 17 Hz   | 1.38 | 3.9 dB   |
| Peaking | 43 Hz   | 2.08 | -1.2 dB  |
| Peaking | 2704 Hz | 3.44 | 2.1 dB   |
| Peaking | 3558 Hz | 4.18 | -3.3 dB  |
| Peaking | 4707 Hz | 9.97 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 8.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Wired%20Mode/V-Moda%20Crossfade%20Wireless%20Wired%20Mode.png)