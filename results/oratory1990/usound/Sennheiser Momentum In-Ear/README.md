# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -8.5; 23 -8.8; 25 -9.0; 28 -9.2; 31 -9.3; 34 -9.3; 37 -9.2; 41 -9.1; 45 -9.1; 49 -9.2; 54 -9.2; 60 -9.4; 66 -9.6; 72 -9.9; 79 -10.1; 87 -10.4; 96 -10.6; 106 -10.8; 116 -11.0; 128 -11.1; 141 -11.1; 155 -11.0; 170 -10.8; 187 -10.6; 206 -10.2; 227 -9.7; 249 -9.1; 274 -9.5; 302 -8.8; 332 -8.1; 365 -7.5; 402 -6.8; 442 -6.1; 486 -5.3; 535 -4.6; 588 -3.8; 647 -3.0; 712 -2.1; 783 -1.3; 861 -0.6; 947 -0.1; 1042 0.1; 1146 0.2; 1261 0.2; 1387 0.3; 1526 0.4; 1678 0.6; 1846 0.8; 2031 0.9; 2234 0.8; 2457 0.8; 2703 1.0; 2973 1.4; 3270 1.9; 3597 2.2; 3957 2.3; 4353 2.2; 4788 1.5; 5267 -0.0; 5793 -2.9; 6373 -7.5; 7010 -10.7; 7711 -10.4; 8482 -7.3; 9330 -5.9; 10263 -6.3; 11289 -6.4; 12418 -7.0; 13660 -6.2; 15026 -3.6; 16529 -2.3; 18182 -0.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.15 | -8.7 dB  |
| Peaking | 224 Hz   | 0.55 | -5.4 dB  |
| Peaking | 5278 Hz  | 0.7  | 6.5 dB   |
| Peaking | 7095 Hz  | 1.83 | -15.1 dB |
| Peaking | 12527 Hz | 1.07 | -6.7 dB  |
| Peaking | 228 Hz   | 2.45 | 1.3 dB   |
| Peaking | 446 Hz   | 0.49 | -1.0 dB  |
| Peaking | 936 Hz   | 1.26 | 1.8 dB   |
| Peaking | 2684 Hz  | 3.03 | -0.7 dB  |
| Peaking | 4849 Hz  | 5.05 | 0.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)