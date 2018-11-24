# Sennheiser PXC 550 Wires ANC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.3; 28 4.3; 31 3.5; 34 3.0; 37 2.7; 41 2.4; 45 2.4; 49 2.6; 54 2.7; 60 2.8; 66 3.0; 72 3.0; 79 3.0; 87 2.8; 96 2.6; 106 2.3; 116 1.9; 128 1.4; 141 1.1; 155 0.8; 170 1.0; 187 0.9; 206 1.0; 227 1.3; 249 1.6; 274 2.1; 302 2.6; 332 3.0; 365 3.2; 402 3.2; 442 3.2; 486 2.8; 535 2.5; 588 2.6; 647 2.3; 712 1.9; 783 1.8; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 0.6; 1387 -1.2; 1526 -1.8; 1678 -2.1; 1846 -0.4; 2031 -0.7; 2234 -0.2; 2457 1.1; 2703 2.8; 2973 3.5; 3270 3.9; 3597 2.2; 3957 3.1; 4353 5.8; 4788 -3.0; 5267 -2.4; 5793 3.6; 6373 4.5; 7010 1.8; 7711 -0.7; 8482 -3.4; 9330 -4.4; 10263 -1.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wires ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wires ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 425 Hz  |  1.23 | 3.3 dB  |
| Peaking | 3317 Hz |  2.77 | 4.1 dB  |
| Peaking | 6327 Hz |  6.72 | 5.4 dB  |
| Peaking | 9019 Hz |  4.38 | -5.1 dB |
| Peaking | 20 Hz   |  1.18 | 5.8 dB  |
| Peaking | 76 Hz   |  1.05 | 2.7 dB  |
| Peaking | 1606 Hz |  3.65 | -2.6 dB |
| Peaking | 4313 Hz |  9.36 | 5.9 dB  |
| Peaking | 4975 Hz | 10.19 | -7.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wires%20ANC%20Active/Sennheiser%20PXC%20550%20Wires%20ANC%20Active.png)