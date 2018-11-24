# Parrot Zik2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -11.3; 23 -10.9; 25 -10.4; 28 -9.5; 31 -8.7; 34 -7.9; 37 -7.3; 41 -6.6; 45 -6.0; 49 -5.5; 54 -5.0; 60 -4.4; 66 -3.8; 72 -3.4; 79 -2.8; 87 -2.4; 96 -1.9; 106 -1.3; 116 -0.7; 128 -0.4; 141 0.0; 155 0.2; 170 0.5; 187 0.8; 206 1.2; 227 1.5; 249 1.6; 274 1.8; 302 2.0; 332 2.3; 365 2.6; 402 2.6; 442 2.9; 486 3.0; 535 3.0; 588 3.3; 647 3.5; 712 3.3; 783 2.9; 861 1.7; 947 0.6; 1042 -0.3; 1146 -0.8; 1261 -1.9; 1387 -2.9; 1526 -4.9; 1678 -7.3; 1846 -8.0; 2031 -7.4; 2234 -6.2; 2457 -4.5; 2703 -0.7; 2973 2.1; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.4; 5267 0.6; 5793 1.7; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -4.6; 10263 -7.0; 11289 -5.4; 12418 -3.9; 13660 -2.5; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Parrot Zik2 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Parrot Zik2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.6  | -11.2 dB |
| Peaking | 63 Hz    | 0.94 | -1.3 dB  |
| Peaking | 1902 Hz  | 0.77 | -26.2 dB |
| Peaking | 2890 Hz  | 0.2  | 18.8 dB  |
| Peaking | 10533 Hz | 0.92 | -14.4 dB |
| Peaking | 663 Hz   | 4.4  | 1.1 dB   |
| Peaking | 2473 Hz  | 4.66 | -3.5 dB  |
| Peaking | 3668 Hz  | 1.45 | 2.9 dB   |
| Peaking | 5299 Hz  | 4.85 | -5.5 dB  |
| Peaking | 6670 Hz  | 9.41 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Parrot%20Zik2%20Bluetooth/Parrot%20Zik2%20Bluetooth.png)