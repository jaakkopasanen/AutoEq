# Pendulumic Stance S1 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 4.8; 49 3.5; 54 2.1; 60 0.7; 66 -0.4; 72 -1.4; 79 -2.1; 87 -2.8; 96 -3.5; 106 -3.7; 116 -3.7; 128 -3.8; 141 -3.8; 155 -3.7; 170 -3.5; 187 -3.2; 206 -3.2; 227 -3.0; 249 -2.9; 274 -2.7; 302 -2.6; 332 -2.9; 365 -2.5; 402 -2.3; 442 -1.8; 486 -1.1; 535 -0.4; 588 0.6; 647 0.9; 712 0.5; 783 -0.1; 861 -0.6; 947 -0.0; 1042 -0.2; 1146 -0.9; 1261 -2.2; 1387 -2.2; 1526 -2.0; 1678 -2.6; 1846 -1.7; 2031 0.3; 2234 2.4; 2457 4.0; 2703 4.7; 2973 3.2; 3270 3.9; 3597 6.0; 3957 3.8; 4353 1.4; 4788 2.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -1.1; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pendulumic Stance S1 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pendulumic Stance S1 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.51 | 12.4 dB |
| Peaking | 78 Hz    | 0.38 | -9.0 dB |
| Peaking | 3320 Hz  | 2.2  | 4.9 dB  |
| Peaking | 5827 Hz  | 3.68 | 6.3 dB  |
| Peaking | 24000 Hz | 2.47 | 4.2 dB  |
| Peaking | 390 Hz   | 2.54 | -1.1 dB |
| Peaking | 632 Hz   | 2.42 | 1.9 dB  |
| Peaking | 1629 Hz  | 1.72 | -3.1 dB |
| Peaking | 2411 Hz  | 4.34 | 3.5 dB  |
| Peaking | 9140 Hz  | 4.68 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pendulumic%20Stance%20S1%20Bluetooth/Pendulumic%20Stance%20S1%20Bluetooth.png)