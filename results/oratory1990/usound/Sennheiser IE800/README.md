# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.2; 28 -11.1; 31 -11.1; 34 -11.1; 37 -11.0; 41 -11.0; 45 -11.0; 49 -11.0; 54 -11.0; 60 -11.0; 66 -11.0; 72 -11.1; 79 -11.1; 87 -11.1; 96 -11.1; 106 -11.0; 116 -10.9; 128 -10.9; 141 -11.0; 155 -11.1; 170 -10.9; 187 -10.7; 206 -10.3; 227 -9.9; 249 -9.5; 274 -9.1; 302 -8.8; 332 -8.4; 365 -8.1; 402 -7.8; 442 -7.5; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.6; 712 -6.4; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -6.7; 1526 -6.1; 1678 -5.2; 1846 -3.9; 2031 -2.7; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -3.3; 5793 -3.8; 6373 -2.8; 7010 -5.3; 7711 -7.1; 8482 -8.5; 9330 -10.5; 10263 -12.7; 11289 -13.0; 12418 -13.3; 13660 -15.1; 15026 -15.3; 16529 -12.5; 18182 -11.3; 20000 -15.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-64**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.37 | -4.1 dB  |
| Peaking | 142 Hz   | 0.32 | -4.2 dB  |
| Peaking | 1337 Hz  | 0.97 | -6.8 dB  |
| Peaking | 5138 Hz  | 0.22 | 15.4 dB  |
| Peaking | 11757 Hz | 0.32 | -18.3 dB |
| Peaking | 2362 Hz  | 6.68 | 0.8 dB   |
| Peaking | 5495 Hz  | 7.42 | -1.6 dB  |
| Peaking | 6333 Hz  | 6.91 | 1.7 dB   |
| Peaking | 17922 Hz | 1.89 | 3.8 dB   |
| Peaking | 20002 Hz | 0.51 | -3.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE800/Sennheiser%20IE800.png)