# Sennheiser PXC 550 Bluetooth ANC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.7; 28 2.1; 31 2.1; 34 2.2; 37 2.3; 41 2.6; 45 2.8; 49 3.0; 54 3.2; 60 3.5; 66 3.6; 72 3.6; 79 3.6; 87 3.4; 96 3.0; 106 2.6; 116 2.4; 128 2.0; 141 1.7; 155 1.5; 170 1.8; 187 1.8; 206 2.0; 227 2.3; 249 2.6; 274 3.0; 302 3.4; 332 3.5; 365 3.6; 402 3.4; 442 3.3; 486 2.9; 535 2.6; 588 2.7; 647 2.4; 712 2.1; 783 2.0; 861 1.1; 947 0.4; 1042 -0.3; 1146 -0.7; 1261 0.1; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -0.7; 2031 -0.9; 2234 -0.2; 2457 1.1; 2703 2.8; 2973 3.5; 3270 4.3; 3597 3.2; 3957 3.7; 4353 6.0; 4788 -1.3; 5267 -2.2; 5793 3.8; 6373 4.8; 7010 2.5; 7711 -0.2; 8482 -3.3; 9330 -4.6; 10263 -1.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Bluetooth ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Bluetooth ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 42 Hz    |  0.06 | 3.0 dB  |
| Peaking | 3553 Hz  |  2.52 | 4.5 dB  |
| Peaking | 6481 Hz  |  4.9  | 6.1 dB  |
| Peaking | 9455 Hz  |  2.1  | -6.9 dB |
| Peaking | 10757 Hz |  2.58 | 3.9 dB  |
| Peaking | 170 Hz   |  1    | -3.3 dB |
| Peaking | 674 Hz   |  0.13 | 2.6 dB  |
| Peaking | 1199 Hz  |  0.7  | -2.8 dB |
| Peaking | 1670 Hz  |  2.02 | -2.9 dB |
| Peaking | 5064 Hz  | 12.62 | -7.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active.png)