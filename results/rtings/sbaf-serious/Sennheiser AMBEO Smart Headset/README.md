# Sennheiser AMBEO Smart Headset

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 2.7; 25 1.8; 28 0.8; 31 0.1; 34 -0.4; 37 -0.8; 41 -1.3; 45 -1.7; 49 -2.0; 54 -2.3; 60 -2.9; 66 -3.3; 72 -3.6; 79 -3.9; 87 -4.4; 96 -4.9; 106 -5.5; 116 -6.0; 128 -6.5; 141 -6.9; 155 -7.0; 170 -7.0; 187 -6.9; 206 -7.0; 227 -6.9; 249 -6.6; 274 -6.1; 302 -5.3; 332 -4.6; 365 -3.9; 402 -3.3; 442 -2.6; 486 -1.8; 535 -1.1; 588 -0.4; 647 0.3; 712 0.9; 783 1.2; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.7; 1526 -2.1; 1678 -2.0; 1846 -1.4; 2031 -0.6; 2234 0.7; 2457 2.1; 2703 3.3; 2973 4.1; 3270 4.7; 3597 4.6; 3957 3.0; 4353 1.0; 4788 1.0; 5267 1.6; 5793 0.7; 6373 -2.9; 7010 -2.5; 7711 -1.2; 8482 -4.9; 9330 -10.3; 10263 -9.4; 11289 -3.2; 12418 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser AMBEO Smart Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser AMBEO Smart Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 20 Hz    |  2.32 | 4.5 dB   |
| Peaking | 132 Hz   |  0.68 | -5.8 dB  |
| Peaking | 256 Hz   |  1.33 | -3.6 dB  |
| Peaking | 3328 Hz  |  2.57 | 5.4 dB   |
| Peaking | 9651 Hz  |  3.71 | -11.9 dB |
| Peaking | 773 Hz   |  2.67 | 2.2 dB   |
| Peaking | 1600 Hz  |  1.81 | -2.5 dB  |
| Peaking | 2540 Hz  |  3.9  | 1.6 dB   |
| Peaking | 6573 Hz  | 12.38 | -3.2 dB  |
| Peaking | 12505 Hz |  4.81 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20AMBEO%20Smart%20Headset/Sennheiser%20AMBEO%20Smart%20Headset.png)