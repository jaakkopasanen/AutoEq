# Scosche RH1060 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -2.1; 23 -2.9; 25 -3.5; 28 -4.3; 31 -4.9; 34 -5.4; 37 -5.7; 41 -6.1; 45 -6.4; 49 -6.7; 54 -6.9; 60 -7.2; 66 -7.4; 72 -7.6; 79 -7.7; 87 -7.9; 96 -8.0; 106 -8.0; 116 -7.9; 128 -7.8; 141 -7.7; 155 -8.0; 170 -7.0; 187 -6.6; 206 -6.4; 227 -5.7; 249 -5.4; 274 -4.1; 302 -2.6; 332 -1.6; 365 0.4; 402 2.3; 442 3.7; 486 4.2; 535 4.4; 588 4.6; 647 3.7; 712 2.3; 783 1.6; 861 0.9; 947 0.3; 1042 0.0; 1146 0.2; 1261 0.2; 1387 -0.2; 1526 -0.7; 1678 -1.5; 1846 -1.9; 2031 -1.7; 2234 -1.5; 2457 -1.7; 2703 -1.9; 2973 -2.0; 3270 -2.6; 3597 -2.1; 3957 -1.3; 4353 -0.7; 4788 -2.6; 5267 -1.1; 5793 2.8; 6373 4.4; 7010 2.5; 7711 -0.5; 8482 -1.9; 9330 -0.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Scosche RH1060 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Scosche RH1060 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.42 | -5.9 dB |
| Peaking | 219 Hz  | 0.5  | -5.7 dB |
| Peaking | 493 Hz  | 1.12 | 8.5 dB  |
| Peaking | 3647 Hz | 0.47 | -2.4 dB |
| Peaking | 6374 Hz | 4.34 | 6.6 dB  |
| Peaking | 3362 Hz | 4.95 | -0.8 dB |
| Peaking | 4570 Hz | 2.3  | 1.6 dB  |
| Peaking | 4884 Hz | 7.62 | -3.3 dB |
| Peaking | 8340 Hz | 5.52 | -2.7 dB |
| Peaking | 9311 Hz | 1.31 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Scosche%20RH1060%20Bluetooth/Scosche%20RH1060%20Bluetooth.png)