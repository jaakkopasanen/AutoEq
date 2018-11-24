# Bose SoundWear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.7; 106 5.5; 116 5.6; 128 5.4; 141 4.3; 155 3.0; 170 1.7; 187 1.7; 206 2.5; 227 5.6; 249 3.7; 274 2.7; 302 1.3; 332 0.3; 365 1.5; 402 -2.0; 442 -1.9; 486 -2.2; 535 -3.9; 588 -2.5; 647 0.1; 712 -1.5; 783 -3.1; 861 -3.2; 947 -1.5; 1042 0.3; 1146 -0.3; 1261 -2.5; 1387 2.1; 1526 3.2; 1678 2.9; 1846 -0.2; 2031 -3.4; 2234 -4.3; 2457 -2.9; 2703 -3.1; 2973 -3.6; 3270 -5.4; 3597 -5.7; 3957 -4.8; 4353 -7.9; 4788 -6.8; 5267 -4.9; 5793 1.6; 6373 1.9; 7010 2.5; 7711 0.3; 8482 -2.7; 9330 -4.7; 10263 -0.6; 11289 0.0; 12418 -1.8; 13660 -5.3; 15026 -6.3; 16529 -1.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundWear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundWear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.17 | 5.1 dB  |
| Peaking | 252 Hz   | 0.16 | 3.6 dB  |
| Peaking | 567 Hz   | 0.84 | -6.1 dB |
| Peaking | 3816 Hz  | 1.54 | -7.1 dB |
| Peaking | 14534 Hz | 3    | -7.1 dB |
| Peaking | 1600 Hz  | 9.22 | 6.1 dB  |
| Peaking | 2170 Hz  | 4.32 | -3.4 dB |
| Peaking | 6559 Hz  | 4.41 | 5.0 dB  |
| Peaking | 8800 Hz  | 7.15 | -1.6 dB |
| Peaking | 9208 Hz  | 8.43 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundWear/Bose%20SoundWear.png)