# Sennheiser MM 550 Travel Bluetooth NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 5.1; 66 4.6; 72 4.2; 79 3.7; 87 3.2; 96 2.7; 106 2.8; 116 3.0; 128 2.5; 141 3.8; 155 3.7; 170 3.7; 187 4.0; 206 3.3; 227 2.4; 249 1.6; 274 0.8; 302 -0.3; 332 -2.0; 365 -3.1; 402 -2.8; 442 -2.5; 486 -1.9; 535 -1.1; 588 -0.6; 647 -0.0; 712 0.5; 783 0.5; 861 0.5; 947 0.2; 1042 -0.4; 1146 -1.5; 1261 -3.1; 1387 -5.2; 1526 -7.8; 1678 -9.5; 1846 -10.3; 2031 -9.4; 2234 -7.0; 2457 -4.0; 2703 -1.2; 2973 0.8; 3270 2.6; 3597 5.0; 3957 6.0; 4353 4.6; 4788 1.3; 5267 2.6; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -2.4; 11289 -2.3; 12418 -0.1; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550 Travel Bluetooth NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550 Travel Bluetooth NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.48 | 6.5 dB   |
| Peaking | 177 Hz   | 2.7  | 3.4 dB   |
| Peaking | 1849 Hz  | 2.06 | -11.5 dB |
| Peaking | 3782 Hz  | 2.83 | 7.2 dB   |
| Peaking | 6107 Hz  | 5.01 | 6.2 dB   |
| Peaking | 274 Hz   | 1.49 | 2.5 dB   |
| Peaking | 371 Hz   | 1.56 | -5.0 dB  |
| Peaking | 876 Hz   | 1.25 | 2.0 dB   |
| Peaking | 1470 Hz  | 4.76 | -1.8 dB  |
| Peaking | 10671 Hz | 4.36 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC/Sennheiser%20MM%20550%20Travel%20Bluetooth%20NC.png)